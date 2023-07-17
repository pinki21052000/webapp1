import streamlit as st
from PIL import Image, ImageFilter,ImageFilter,ImageFont,ImageDraw
import os


#create folder Images
#pillow for image
if not os.path.exists('images'):
  os.makedirs('images')
def save_image(image):
  img=Image.open(image)
  img.save(f'images/{image.name}.png')
st.title('🖼️Image Processing App') 
upload=st.file_uploader( 
    label='Uplaod your image',
    type=['jpg','png','jpeg']      
) 
if upload is not None:
  save_image(upload)
  img=Image.open(upload)
  col1, col2= st.columns(2)

  filters =['countour','emboss','edge_enchance','blur','smooth','sharpen']
  option=st.sidebar.selectbox('selects a filter',filters)
  col1.image(upload, caption='Upload Image',use_column_width=True)
  if option =='countour':
    col2.image(img.filter(ImageFilter.CONTOUR), caption='Countour Filter', use_column_width=True)
  if option =='emboss':
    col2.image(img.filter(ImageFilter.EMBOSS), caption='Emboss Filter', use_column_width=True)
  if option =='edge_enchance':
    col2.image(img.filter(ImageFilter.EDGE_ENHANCE), caption='Edge_enchance', use_column_width=True)
  if option =='blur':
    col2.image(img.filter(ImageFilter.BLUR), caption='Blur', use_column_width=True)
  if option =='smooth':
    col2.image(img.filter(ImageFilter.SMOOTH), caption='Smooth', use_column_width=True)
  if option =='sharpen':
    col2.image(img.filter(ImageFilter.SHARPEN), caption='Sharpen', use_column_width=True)
  message=st. text_input("Enter a message",value='JIMMY')
  font_size= st.sidebar.number_input("Enter font size",value=20)
  font_color= st.sidebar.color_picker('select font color')
  c1,c2=st.sidebar.columns(2)
  x=c1.number_input('X coordinate', value=img.width//2)
  y=c2.number_input ('Y cordinate',value =img.height//2 )
  #copy img to another
  imgc=img.copy()
  draw= ImageDraw.Draw(imgc)
  font=ImageFont.truetype('myfont.ttf',font_size)
  draw.text((x,y),message,font_color,font)
  st.image(imgc,width=300)

