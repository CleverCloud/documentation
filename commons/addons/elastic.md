---
title: Elastic Stack add-on
position: 7
shortdesc: The Elastic Stack is Elasticsearch, Kibana, Beats, and Logstash (also known as the ELK Stack). 
tags:
- addons
keywords:
- fulltext
- elsaticsearch
- elastic
- kibana
- apm
---

The Elastic Stack is Elasticsearch, Kibana, Beats, and Logstash (also known as the ELK Stack). Reliably and securely take data from any source, in any format, then search, analyze, and visualize it in real time. Find out more about it on [Elastic's website](https://www.elastic.co/products/elastic-stack).

Provisioning the Elastic Stack addon on Clever Cloud will give you an Elasticsearch instance, Kibana and an APM server.

## Elastic Stack version

The current versions supported at add-on creation are 6 and 7.

## Elasticsearch

Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores your data so you can discover the expected and uncover the unexpected.

## Kibana

Kibana lets you visualize your Elasticsearch data and navigate the Elastic Stack so you can do anything from tracking query load to understanding the way requests flow through your apps.

It is available as an opt-in option of the Elastic add-on. It will be deployed and billed as a regular application. You can upscale/downscale/delete it at any time. This application will be updated by Clever Cloud on a regular basis.

The created application name follow the pattern *Kibana - elasticsearch_addon_eb464a6d-ce5f-4780-b595-6772ebe33d06*.

Learn more on [Kibana official documentation](https://www.elastic.co/guide/en/kibana/current/index.html).

### Authentication

Any member of the Clever Cloud organisation containing the Elastic add-on will be able to login to Kibana through an automatically configured SSO system. 

## Elastic APM

Elastic APM is an Application performance management tool chain based on the Elastic Stack. See exactly where your application is spending time so you can quickly fix issues and feel good about the code you push. To use it you must install an *APM agent* to your application. Once both your application and APM server are running, you application with automatically send APM datas to the APM server wich will send them to Elastic and once indexed they will be available in your Kibana dashboard (this process is really fast, you won't see it as a human).

Curently, APM agents are available in the following languages:
- [Go](https://www.elastic.co/guide/en/apm/agent/go/1.x/introduction.html)
- [Java](https://www.elastic.co/guide/en/apm/agent/java/1.x/intro.html)
- [Node.js](https://www.elastic.co/guide/en/apm/agent/nodejs/2.x/intro.html)
- [Python](https://www.elastic.co/guide/en/apm/agent/python/5.x/getting-started.html)
- [Ruby](https://www.elastic.co/guide/en/apm/agent/ruby/3.x/introduction.html)

It is available as an opt-in option of the Elastic add-on. It will be deployed and billed as a regular application. You can upscale/downscale/delete it at any time. This application will be updated by Clever Cloud on a regular basis.

The created application name follow the pattern *APM - elasticsearch_addon_eb464a6d-ce5f-4780-b595-6772ebe33d06*.  

Learn more on [APM official documentation](https://www.elastic.co/guide/en/apm/get-started/current/components.html).

### How to setup APM

Any applications linked to the APM application will have the right credentials and APM endpoint automatically avaiable as environment variables. These variables can be picked up automatically by the APM agent you are using in your application. As such everything should work automatically.

## Elastic stack plans

<table class="table table-bordered table-striped dataTable"><caption>Elastic Stack pricing plans</caption> 
    <tbody>
        <tr>
          <th><strong>Plan name </strong></th>
            <th> CPUs </th>
            <th> DISK </th>
            <th> MEMORY </th>
            <th> NODES </th>
            <th> Price </th>
        </tr>
          <tr>
            <td class="cc-col__price"><span class="label cc-label__price label-info">XS</span></td>
              <td>1</td>
              <td>10</td>
              <td>1</td>
              <td>1</td>
              <td>17.00&nbsp;€</td>
          </tr>
          <tr>
            <td class="cc-col__price"><span class="label cc-label__price label-info">S</span></td>
              <td>1</td>
              <td>60</td>
              <td>2</td>
              <td>1</td>
              <td>34.00&nbsp;€</td>
          </tr>
          <tr>
            <td class="cc-col__price"><span class="label cc-label__price label-info">M</span></td>
              <td>2</td>
              <td>120</td>
              <td>4</td>
              <td>1</td>
              <td>58.00&nbsp;€</td>
          </tr>
          <tr>
            <td class="cc-col__price"><span class="label cc-label__price label-info">L</span></td>
              <td>4</td>
              <td>240</td>
              <td>8</td>
              <td>1</td>
              <td>122.00&nbsp;€</td>
          </tr>
          <tr>
            <td class="cc-col__price"><span class="label cc-label__price label-info">XL</span></td>
              <td>6</td>
              <td>450</td>
              <td>16</td>
              <td>1</td>
              <td>237.00&nbsp;€</td>
          </tr>
          <tr>
            <td class="cc-col__price"><span class="label cc-label__price label-info">XXL</span></td>
              <td>8</td>
              <td>870</td>
              <td>32</td>
              <td>1</td>
              <td>458.00&nbsp;€</td>
          </tr>
          <tr>
            <td class="cc-col__price"><span class="label cc-label__price label-info">XXXL</span></td>
              <td>16</td>
              <td>1700</td>
              <td>64</td>
              <td>1</td>
              <td>967.00&nbsp;€</td>
        </tr>
        <tr>
            <td class="cc-col__price"><span class="label cc-label__price label-info">4XL</span></td>
              <td>32</td>
              <td>3500</td>
              <td>128</td>
              <td>1</td>
              <td>1887.00&nbsp;€</td>
          </tr>
          <tr>
            <td class="cc-col__price"><span class="label cc-label__price label-info">5XL</span></td>            
              <td>64</td>            
              <td>7000</td>            
              <td>256</td>            
              <td>1</td>            
              <td>4151.00&nbsp;€</td>
          </tr>        
    </tbody>
</table>


