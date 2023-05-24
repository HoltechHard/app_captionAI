# app_captionAI
Group 03 - System for generating titles from images  

* Deployement:  
  Full-repository of appTIGenAI_v8.0  
  https://mega.nz/folder/RtFAWTLJ#drYIXBrhT2GmgQmBNQAwCA  

* Functional Aspects:  

1) Dataset  
COCO - Common objects in conext (Microsoft)  
https://cocodataset.org/#home  

2) DL Model  
Visual Encoder-Decoder Model (ViT + GPT-2)  
Link: https://huggingface.co/docs/transformers/v4.29.1/en/model_doc/vision-encoder-decoder#transformers.VisionEncoderDecoderModel  

![vision-encoder-decoder](https://github.com/HoltechHard/app_captionAI/assets/35493202/73fe6cc2-2741-4b20-838d-ec5e05821338)


Comment:  
The Visual Encoder-Decoder Model can be used to initialize an image-to-text model with:  
Step 01: Pretrained transformer-based vision model ==> this is the encoder (ViT)  
Step 02: Pretrained language model ==> this is the decoder (GPT-2)  

3) Software Application  
Will consist of 3 stages:  
- Module 1: information system to upload and show images  
  Tools: Python + Django + Jquery + Frontend (not defined)  
- Module 2: system with elements of AI with integration of ViT + GPT-2 model to Module 1  
  Tools: PyTorch DL Framework  
- Module 3: scalability of the system and upload all components of Module 2 in some container  
  Tools: still undefined (probable Docker and some orchestrator to manage all libraries and components of Module 2)  

4) Documentation  
  (Still undefined)  
  Will be necessary read documents inside of folder "papers" and compress all the technical aspects involved 
  in out project in this related with the 2 aspects: Dataset and DL Model and for the 3rd aspect: Software Application
  will be necessary apply some Software Methodology for documentation (RUP, SCRUM, Agile Methods, etc...)
  
