# AWS

Project to test local development of serverless app with AWS SAM,CI/CD this uses only python

tips:

    layers:
    
    -layers can be built before functions
    -with pycharm imports from a layer will not  show import error "even if they are not in the same dir as the func that uses it"
    -must use a makefile to create the correct folder structure with custom .py files and the respective requirements , if you only need whats in your
    requirements.txt for that layer then using python3.x as BuildMethod is more than enough
    -do not zip the layer folder the input for deployment is a directory not a zip file
        
    
    functions:
    -use --skip-pull-image to avoid fetching(this takes an insane amount of time) eacht ime you build your function, but i recommend fetching it at 
    leas once to ahve the latest container image
    -all functions require their own independant directory with its __init__ file
    -you can test the whole api(rather than each function individually) using  "sam local start-api"
    
    env variables:
    -locally use an env,json which will asing custom values to these env variables, you'll need to add --env-vars "path" to the invoke call
     keep in mind that the path must be a absolute path cant make it work with a relative path so far
     
    credentials:
    -for local build no credentials are needed, but some IDE's will ask you to give a default one anyways
    
        