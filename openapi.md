+++
weight = 1
chapter = false
title = "API documentation"
toc = false
disableReadmoreNav = true
disableComments = true
type = "openapi"
+++

<!-- Fix because Hugo wraps the <rapi-doc> in a <p> (not recognized as a standard HTML tag) -->
<div style="height: 100%;">
<rapi-doc spec-url="https://api.clever-cloud.com/v2/openapi.json"
    show-header = 'false'
    show-info = 'true'
    allow-try="false" 
    allow-search="true" 
    allow-authentication ='false'
    allow-server-selection = 'false'
    allow-api-list-style-selection ='true'
    nav-bg-color='#13172e'
    nav-text-color='rgba(255,255,255,.5)'
    nav-hover-bg-color='#333f54'
    nav-hover-text-color='#ada5ea'
    nav-accent-color='#ada5ea'
    nav-item-spacing='compact'
    primary-color='#bd3839'
    render-style = "focused"
    layout="column">
</rapi-doc>
</div>