# Final Project app_captionAI: Course Developing applications with elements of AI  

## Students
Group 03 - System for generating titles from images  
1st course - Program of Master degree in AI & Machine Learning - Polytech University    
     - Li Siyuan  (coordinator and software development in java)  
     - Holger Espinola  (staff in machine learning engineer + python backend)  
     - Van Syiui  (staff in devops and infrastructure/software deployment)       
     - Zhen Menguan  (staff in database development)  
     - Artur Magomedov  (staff in testing and QA-analyst)  
     - Fiodor Babeliuk  (staff in testing and system requirements)  

### Web page:  
http://192.168.199.88/  
  
## Functional Aspects:  

1) Dataset  
COCO - Common objects in conext (Microsoft)  
https://cocodataset.org/#home  

2) DL Model  
Visual Encoder-Decoder Model (ViT + GPT-2)  
Link: https://huggingface.co/docs/transformers/v4.29.1/en/model_doc/vision-encoder-decoder#transformers.VisionEncoderDecoderModel  

![vision-encoder-decoder](https://github.com/HoltechHard/app_captionAI/assets/35493202/73fe6cc2-2741-4b20-838d-ec5e05821338)

ML-Architecture:  
The Visual Encoder-Decoder Model architecture of DL-model to generate captions from images consists of 2 blocks:  
Block 01: Pretrained transformer-based vision model ==> this is the encoder (ViT)  
Block 02: Pretrained language model ==> this is the decoder (GPT-2)  

3) Software Application  
Developing of system consist of 5 stages:  
- Stage 1: software system integrated to AI model Encoder-Decoder Transformer ViT + GPT-2  
  Tools: PyTorch DL Framework + mini-app in Python + Django + Jquery  
  Github repo: finalAppCaptionAI-ml-algorithm [https://github.com/Team03captionAI/finalAppCaptionAI-ml-algorithm]  
  VisionEncoderDecoderModel  
    
  ![image](https://github.com/Team03captionAI/Presentation/assets/35493202/553141d4-c7d8-40c9-8e6a-172b8d6cea7e)  
    
  GPT-2 Tokenizer    
    
  ![image](https://github.com/Team03captionAI/Presentation/assets/35493202/d73b7930-96e8-4503-b3f0-546bed5278f3)  

- Stage 2: frontend module
  Tools: HTML + Javascript + Vue  
  Github repo: finalAppCaptionAI-frontend [https://github.com/Team03captionAI/finalAppCaptionAI-frontend]   
  
  Main web page:  
    
  ![image](https://github.com/Team03captionAI/Presentation/assets/35493202/c08b2281-88c7-4d9b-818a-ebf6b82a2e6d)  
  
- Stage 3: database module
   
  Physical database model:  
    
  ![database_model](https://github.com/Team03captionAI/Presentation/assets/35493202/3f48ef5d-228b-4c7d-bc37-85b8e3e99d10)
    
  Tools: MySQL  
  
- Stage 4: backend module  
  Tools: Java Spring Boot + Spring Security + myBatis 
  Github repo: finalAppCaptionAI-java-backend [https://github.com/Team03captionAI/finalAppCaptionAI-java-backend]  
  
- Stage 5: software deployment  
The front-end, back-end and algorithm of the project are separate parts. In order to realize the reuse and rapid deployment of the algorithm, a corresponding docker image was made, which can be found on the [docker hub](https://hub.docker.com/repository/docker/wsyconan/caption_ai/general).

The default deployment address of this image is 0.0.0.0:5000.

We use the algorithm through http requests, and the format is:

**Request**

Method：POST

HEADER：

Content-Type: multipart/form-data
X-CSRFToken: xxxxxxxx

BODY:

Content-Disposition: form-data; name="images"; filename="image_name.png"

Content-Type: image

[image data]

**Response**

If the prediction success, the response will be：

HTTP/1.1 200 OK

{

"image_name": "caption"

}
