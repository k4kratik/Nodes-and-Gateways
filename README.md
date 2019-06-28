# Nodes-and-Gateways
_A simple yet elegant node and gateway manager_

#### Description -
This is a Web App to manage Nodes & Clusters in an Organization where a authenticated user can create "Gateway" and "Node".

#### The Web App has Following Modules - 
1. User -  
* A user can create an account in the  web application. 
* A user can log in to the website and 
* A user can log out from the website.

2. Blocks - 
* It displays different blocks of an organization campus.
* Only Admin is allowed to create blocks.
* One block can be consisted of multiple nodes.

3. Gateway - 
* There can be multiple gateways in an organization campus.
* An authenticated user can create multiple gateways.
* Each gateway can have multiple nodes as children.
* when an authenticated user creates a gateway then the user will be redirected to a node creation form.

4. Node -
* There can be multiple nodes in an organization campus.
* There can be multiple nodes attached to single Gateway.
* There can be multiple nodes in a block.
*  An authenticated user can create multiple Nodes.

Tech Stack - HTML, Bootstrap4, Python 3, Django 2.2, SQLite db