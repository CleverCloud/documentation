(function() {
  'use strict';
  
  function ready(fn) {
    if (document.readyState !== 'loading') { 
      fn(); 
    } else { 
      document.addEventListener('DOMContentLoaded', fn); 
    }
  }

  ready(function() {
    // Ensure DocSearch container exists and place it inside the theme search wrapper
    var containerId = 'docsearch';
    var container = document.getElementById(containerId);
    if (!container) {
      container = document.createElement('div');
      container.id = containerId;
      var themeWrapper = document.querySelector('.search-wrapper');
      if (themeWrapper) {
        // Place DocSearch inside the search wrapper
        themeWrapper.appendChild(container);
      } else {
        // Fallback
        var header = document.querySelector('header');
        if (header) {
          header.appendChild(container);
        } else {
          document.body.appendChild(container);
        }
      }
    }

    // Initialize DocSearch (wait if script not loaded yet)
    var openDocSearch;
    var initDocSearch = function() {
      if (!window.docsearch) return false;
      try {
        var docSearchConfig = window.docSearchConfig || {};
        window.docsearch({
          appId: docSearchConfig.appId || '',
          apiKey: docSearchConfig.apiKey || '',
          indexName: docSearchConfig.indexName || '',
          container: '#docsearch',
          debug: false
        });
        openDocSearch = function() {
          var btn = document.querySelector('#docsearch .DocSearch-Button');
          if (btn) { 
            btn.click(); 
          }
        };
        return true;
      } catch (e) { 
        console.error('DocSearch initialization error:', e);
        return false; 
      }
    };
    
    if (!initDocSearch()) {
      var tries = 0;
      (function waitForDocSearch(){
        if (initDocSearch()) return;
        if (tries++ < 30) setTimeout(waitForDocSearch, 100);
      })();
    }

    // Hook the existing theme Search input/button to open DocSearch with prefill
    var tryAttach = function() {
      var header = document.querySelector('header');
      var found = false;

      // 1) Buttons or anchors acting as search triggers
      var btns = header ? header.querySelectorAll([
        'button[aria-label="Search"]',
        'button[aria-label*="search" i]',
        'a[aria-label*="search" i]',
        '.hx-search',
        'button[class*="search" i]',
        'a[class*="search" i]',
        'a[href="#search"]',
        '[role="search"] button',
        '[data-testid*="search" i]',
        '[data-track*="search" i]'
      ].join(',')) : [];
      
      btns.forEach(function(el){
        if (el.__ccDocSearchBound) return; 
        el.__ccDocSearchBound = true; 
        found = true;
        el.addEventListener('click', function(ev){ 
          ev.preventDefault(); 
          if (openDocSearch) openDocSearch(); 
        });
        el.addEventListener('keydown', function(ev){ 
          if (ev.key === 'Enter' || ev.key === ' ') { 
            ev.preventDefault(); 
            if (openDocSearch) openDocSearch(); 
          }
        });
      });

      // 2) The actual input/form used by the theme
      var input = header ? header.querySelector('input[type="search"], input[placeholder*="search" i], .hx-search input, [role="search"] input') 
                         : document.querySelector('input.search-input');
      var form = input ? input.closest('form') : (header ? header.querySelector('form[role="search"], form.hx-search, .hx-search form') : null);

      var ensureOpen = function(cb){
        if (openDocSearch) { 
          cb(); 
          return; 
        }
        var t = 0;
        var tick = function(){
          if (openDocSearch) { 
            cb(); 
            return; 
          }
          if (t++ < 30) setTimeout(tick, 100);
        };
        tick();
      };
      
      var openWithPrefill = function(extraChar) {
        var prefill = '';
        if (input) prefill = (input.value || '');
        if (extraChar && extraChar.length === 1) prefill += extraChar;
        ensureOpen(function(){ 
          openDocSearch(); 
        });
        // After modal mounts, set its input value and propagate event
        setTimeout(function(){
          var modalInput = document.querySelector('.DocSearch-Input');
          if (modalInput) {
            modalInput.value = prefill;
            var evt = new Event('input', { bubbles: true });
            modalInput.dispatchEvent(evt);
            modalInput.focus();
            // Move caret to end
            try { 
              modalInput.setSelectionRange(modalInput.value.length, modalInput.value.length); 
            } catch (e) {}
          }
        }, 20);
      };

      if (input && !input.__ccDocSearchBound) {
        input.__ccDocSearchBound = true; 
        found = true;
        // Prevent typing into the old input; route into DocSearch
        input.addEventListener('focus', function(e){ 
          e.preventDefault(); 
          openWithPrefill(); 
          input.blur(); 
        });
        input.addEventListener('keydown', function(e){
          // Allow Tab to move focus
          if (e.key === 'Tab') return;
          e.preventDefault();
          var ch = (e.key && e.key.length === 1) ? e.key : '';
          if (e.key === 'Backspace') { 
            if (openDocSearch) openWithPrefill(''); 
            return; 
          }
          openWithPrefill(ch);
        });
      }

      if (form && !form.__ccDocSearchBound) {
        form.__ccDocSearchBound = true; 
        found = true;
        form.addEventListener('submit', function(e){ 
          e.preventDefault(); 
          openWithPrefill(); 
        });
      }

      // Overlay approach: add a transparent clickable layer above the input
      var wrapper = (input && input.closest('.search-wrapper')) || document.querySelector('.search-wrapper');
      if (wrapper && !wrapper.querySelector('.cc-docsearch-overlay')) {
        found = true;
        var overlay = document.createElement('button');
        overlay.type = 'button';
        overlay.className = 'cc-docsearch-overlay';
        overlay.setAttribute('aria-label', 'Open search');
        overlay.style.position = 'absolute';
        overlay.style.inset = '0';
        overlay.style.background = 'transparent';
        overlay.style.cursor = 'text';
        overlay.style.zIndex = '5';
        overlay.style.border = '0';
        overlay.style.padding = '0';
        overlay.style.margin = '0';
        // Let the kbd hint remain clickable-less
        var kbd = wrapper.querySelector('kbd');
        if (kbd) { 
          kbd.style.pointerEvents = 'none'; 
        }
        overlay.addEventListener('click', function(e){ 
          e.preventDefault(); 
          openWithPrefill(); 
        });
        overlay.addEventListener('keydown', function(e){
          if (e.key === 'Tab') return;
          e.preventDefault();
          var ch = (e.key && e.key.length === 1) ? e.key : '';
          openWithPrefill(ch);
        });
        wrapper.style.position = wrapper.style.position || 'relative';
        wrapper.appendChild(overlay);
      }

      return found;
    };
    
    if (!tryAttach()) {
      // Retry shortly after to give the theme time to render header
      setTimeout(tryAttach, 200);
      setTimeout(tryAttach, 500);
      // Observe header mutations to rebind when menu/header changes (e.g., responsive)
      var header = document.querySelector('header');
      if (header && !header.__ccDocSearchObserved) {
        header.__ccDocSearchObserved = true;
        var mo = new MutationObserver(function(){ 
          tryAttach(); 
        });
        mo.observe(header, { childList: true, subtree: true });
      }
    }

    // Global keyboard shortcuts to match common UX: '/' and Cmd/Ctrl+K
    window.addEventListener('keydown', function(e){
      var activeTag = (document.activeElement && document.activeElement.tagName) || '';
      var typingInInput = /INPUT|TEXTAREA|SELECT/.test(activeTag);
      if (!typingInInput && (e.key === '/' || (e.key.toLowerCase() === 'k' && (e.metaKey || e.ctrlKey)))) {
        e.preventDefault();
        if (openDocSearch) openDocSearch();
      }
    });
  });
})();