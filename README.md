# AWS serverless
## About

   Project based on a serverless application using SAM and Python3.8,basically is a general CRUD for different databases

## Functionalities

- Postgresql Connection
- MongoDB Connection
- Cognito authentication
- Trigger a sns topic
- Logging
    
## Learned so far

 - layers:
    
    - layers can be built before functions
    
    - with pycharm imports from a layer will not  show import error "even if they are not in the same dir as the func that uses it as long as a __init__ file exists"
    
    - must use a makefile to create the correct folder structure with custom .py files and the respective requirements , if you only need whats in your
      requirements.txt for that layer then using python3.x as BuildMethod is more than enough
        
            build-MyLayer:
                mkdir -p "$(ARTIFACTS_DIR)/python"
                cp *.py "$(ARTIFACTS_DIR)/python"
                python -m pip install -r requirements.txt -t "$(ARTIFACTS_DIR)/python"
  
      take in count that "MyLayer is the name of he function/layer"
  
   - do not zip the layer folder the input because deployment is a directory not a zip file
            
    
 - functions:
 
    - use --skip-pull-image to avoid fetching(this takes an insane amount of time) eacht ime you build your function, but i recommend fetching it at 
    leas once to ahve the latest container image
    - all functions require their own independant directory with its __init__ file
    - you can test the whole api(rather than each function individually) using  "sam local start-api"
        
 - env variables:

    - locally use an env.json which will set custom values to these env variables,you'll need to add --env-vars "path" to the invoke call
      
    - keep in mind that the path must be a absolute path cant make it work with a relative path so far
         
 - credentials:
 
    - for local build no credentials are needed, but some IDE's will ask you to give a default one anyways
        
            