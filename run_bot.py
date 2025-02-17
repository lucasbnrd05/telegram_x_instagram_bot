import telebot
import os, shutil
from PIL import Image
import time
from instagrapi import Client
import random

telegram_api_key = "Your Telegram Key"
bot = telebot.TeleBot(telegram_api_key)

# List of captions to use when posting photos or videos.
# Add your own captions as strings inside the list.
# Example: captions = ["Great view!", "Amazing shot!", "Sunset vibes 🌅"]
captions = []

# List of hashtags to be used when posting content.
# Feel free to modify or add hashtags to fit your needs.
# Example: hagtaglist = ["nature", "travel", "sunset", "explore", "photography"]
hagtaglist = []

# List of comments to be used when interacting with posts.
# You can add or modify comments based on your needs.
# Example: commentlist = ["Awesome post!", "Love this! ❤️", "Great content! Keep it up!"]
commentlist = []

listenom = []
cl = Client()
cl.login("Your instagram name", "Your instagram password")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Here is the list of commands:\n/Set_ : Defines the list of accounts to take content from\n/List_ : Returns the list if filled, otherwise returns an empty list\n/Import_ : Imports a new model\n/Faceswap_ : Faceswap model\n/Publication_ : Publishes every 6 hours\n/Stoppubli_ : Stops publishing\n/Like_ : Likes based on defined hashtags\n/Comment_ : Comments based on hashtags\n/LikeComment_ : Likes and comments based on hashtags\n/AjoutHtag_ : Adds a hashtag\n/SupHtag_ : Removes a hashtag\n/EnumHtag_ : Returns the list if filled, otherwise returns an empty list\n/Listemessage_ : Returns the list of unread messages\n/Respons_ : Allows replying to one or more users with the desired message (format: Respons_user_textresponse,user_textresponse...)\n")
  
@bot.message_handler(regexp="Set_")
def send_welcome(message):
  listenom.extend(message.text[5:].split(','))
  string = "\n".join(listenom)
  bot.reply_to(message, string)

@bot.message_handler(regexp="List_")
def send_welcome(message):
  if listenom:
    bot.reply_to(message, "\n".join(listenom))
  else:
    bot.reply_to(message, "Empty list")

@bot.message_handler(regexp="AjoutHtag_")
def send_welcome(message):
  hagtaglist.extend(message.text[10:].split(','))
  string = "The list of # : \n"
  string += "\n".join(hagtaglist)
  bot.reply_to(message, string)

@bot.message_handler(regexp="SupHtag_")
def send_welcome(message):
  refsup = []
  refsup.extend(message.text[9:].split(','))
  for htag in refsup :
     hagtaglist.remove(htag)
  string = "The list of # : \n"
  string += "\n".join(hagtaglist)
  bot.reply_to(message, string)

@bot.message_handler(regexp="EnumHtag_")
def send_welcome(message):
  if hagtaglist:
    bot.reply_to(message, "\n".join(hagtaglist))
  else:
    bot.reply_to(message, "Empty list")

@bot.message_handler(regexp="Listemessage_")
def send_welcome(message):
    string = "The messages received are : \n"
    dico = cl.direct_threads(10,"unread")
    for dm in dico :
        string += f"{dm.users} : {dm.messages[0].text}\n"
    bot.reply_to(message, string)

@bot.message_handler(regexp="Respons_")
def send_welcome(message):
    #format = user_textrespons,user_textrespons...
    tab = message.text[:9].split(',')
    for rep in tab : 
        mes  = rep.split('_')
        cl.direct_send(mes[1], user_ids=[user_id_from_username(mes[0])])
        time.sleep(5)
    bot.reply_to(message, "All answers are sent")

@bot.message_handler(regexp="Import_")
def send_welcome(message):
  string = ""
  string_ref = ""
  REF = []
  for i in str(message.text[8:]).split(','):
    listenom.append(i)
    string_ref += i + " "
  for i in listenom:
     string += i + "\n"
  os.system(f"python3 -m instaloader  --login 'Your instagram login'  +args.txt {string_ref}")
  L = os.listdir(os.path.abspath("."))
  for i in L:
    for nom in listenom:
        if str(i) == nom and os.path.getsize(i) > 0:
            REF.append(i)
  for fichier in REF :
    for path, dirs, files in os.walk(fichier):
        for filename in files:
            if ".mp4" in filename:
                shutil.move(os.path.abspath(fichier)+"/"+filename, f"{os.path.abspath('mp4')}")
            if ".jpg" in filename:
                shutil.move(os.path.abspath(fichier)+"/"+filename, f"{os.path.abspath('photo')}")
  for path, dirs, files in os.walk('photo'):
    for filename in files:
        if ".jpg" in filename:
            im = Image.open(os.path.abspath('photo')+"/"+f"{filename}")
            im.save(os.path.abspath('photo')+"/"+f"{filename[:-4]}.png", 'PNG')
            os.remove(os.path.abspath('photo')+"/"+f"{filename}")
  bot.reply_to(message, string)

@bot.message_handler(regexp="Faceswap_")
def send_welcome(message):
      def process_files(input_dir, output_dir, conversion_needed=False, pause=25):
          for _, _, files in os.walk(input_dir):
              for filename in files:
                  input_file = os.path.join(input_dir, filename)
                  output_file = os.path.join(output_dir, filename)
                  if conversion_needed and filename.endswith(".jpg"):
                      img = Image.open(input_file)
                      png_output_file = output_file.replace(".jpg", ".png")
                      img.save(png_output_file, 'PNG')
                      os.remove(input_file)
                      input_file = png_output_file
                  os.system(f"python3 roop/run.py -s 'ref.png' -t '{input_file}' -o '{output_file}'")
                  os.remove(input_file)
                  time.sleep(pause)
                  if conversion_needed and filename.endswith(".png"):
                      img = Image.open(output_file)
                      jpg_output_file = output_file.replace(".png", ".jpg")
                      img.save(jpg_output_file, 'JPEG')
                      os.remove(output_file)
      pauses = {
          "photo": 15,
          "mp4": 90,
      }

      process_files('photo', 'photo_swap', pause=pauses['photo'])
      process_files('mp4', 'video_swap', pause=pauses['mp4'])
      bot.reply_to(message, "Faceswapping Endding")

publier = True 
nb = 0
nbphoto = 0
nbvideo = 0

for path, dirs, files in os.walk('photo_swap'):
          nb = len(files) - 1
          nbphoto = len(files) - 1
for path, dirs, files in os.walk('video_swap'):
        nb += len(files) - 1
        nbvideo = len(files) - 1

@bot.message_handler(regexp="Stoppubli_")
def send_welcome(message):
  global publier
  publier = False
  bot.reply_to(message, f"The published variable is a {publier}")

@bot.message_handler(regexp="Publication_")
def send_welcome(message):
  global publier
  global nb, nbphoto, nbvideo
  publier = True
  bot.reply_to(message, f"Start of publications")
  while publier and nb > 0 :  
    nb -= 1
    i = 0
    photoorvideo = random.choice([True,False])
    if photoorvideo and nbphoto > 0:
      nbphoto -= 1
      for path, dirs, files in os.walk('photo_swap'):
          if i < 1 :
            i += 1
            photolink = random.choice(files)
            e = random.choice(captions)
            cl.photo_upload(
                f"photo_swap/{photolink}",
                f"{e}",
                #extra_data={
                #    "custom_accessibility_caption": "alt text example",
                #    "like_and_view_counts_disabled": 1,
                #    "disable_comments": 1,
                #}
            )
            os.remove(os.path.abspath('photo_swap')+"/"+f"{photolink}")
            bot.reply_to(message, f"Photo published and deleted from the file, {nbphoto} photos remaining\nThe file is called: {photolink} and caption = {e}")
    elif not photoorvideo and nbvideo > 0 :
      nbvideo -= 1
      for path, dirs, files in os.walk('video_swap'):
        if i < 1 :
          i += 1
          photolink = random.choice(files)
          e = random.choice(captions)
          cl.clip_upload(
              f"video_swap/{photolink}",
              f"{e}",
          )
          os.remove(os.path.abspath('video_swap')+"/"+f"{photolink}")
          bot.reply_to(message, f"Reel published and deleted from the file, {nbvideo} videos remaining\nThe file is called: {photolink} and caption = {e}")
    elif nbphoto > 0:
      nbphoto -= 1
      for path, dirs, files in os.walk('photo_swap'):
          if i < 1 :
            i += 1
            photolink = random.choice(files)
            e = random.choice(captions)
            cl.photo_upload(
                f"photo_swap/{photolink}",
                f"{e}",
            )
            os.remove(os.path.abspath('photo_swap')+"/"+f"{photolink}")
            bot.reply_to(message, f"Photo published and deleted from the file, {nbphoto} photos remaining\nThe file is called: {photolink} and caption = {e}")
    elif nbvideo > 0 :
      nbvideo -= 1
      for path, dirs, files in os.walk('video_swap'):
        if i < 1 :
          i += 1
          photolink = random.choice(files)
          e = random.choice(captions)
          cl.clip_upload(
              f"video_swap/{photolink}",
              f"{e}",
            )
          os.remove(os.path.abspath('video_swap')+"/"+f"{photolink}")
          bot.reply_to(message, f"Reel published and deleted from the file, {nbvideo} videos remaining\nThe file is called: {photolink} and caption = {e}")
    else : 
       publier = False
       bot.reply_to(message, f"No more data to send")
    timer = 21600 
    bot.reply_to(message, f"Waiting {timer} seconds")
    time.sleep(timer)
  bot.reply_to(message, f"End of publication")

@bot.message_handler(regexp="Like_")
def send_welcome(message):
  for hastag in hagtaglist :
    medias = cl.hashtag_medias_top(hastag, amount=9)
    for publi in medias :
      cl.media_like(publi.dict()['id'])
      time.sleep(40)
  bot.reply_to(message, "Finish liking")

@bot.message_handler(regexp="Comment_")
def send_welcome(message):
  for hastag in hagtaglist :
    medias = cl.hashtag_medias_top(hastag, amount=9)
    for publi in medias :
      cl.media_comment(publi.dict()['id'], f"{random.choice(commentlist)}")
      time.sleep(50)
  bot.reply_to(message, "Finish Commenting")

@bot.message_handler(regexp="LikeComment_")
def send_welcome(message):
  for hastag in hagtaglist :
      medias = cl.hashtag_medias_top(hastag, amount=9)
      for publi in medias :
        cl.media_like(publi.dict()['id'])
        time.sleep(40)
        cl.media_comment(publi.dict()['id'], f"{random.choice(commentlist)}")
        time.sleep(50)
  bot.reply_to(message, "Finish liking and commenting")

bot.infinity_polling()
