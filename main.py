from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import callback_query
import requests,user_agent,json,os,sys,secrets,names,urllib
from user_agent import generate_user_agent
import logging
import random, datetime
from faker import Faker 
from time import sleep
bot = Bot(token='5734388256:AAHFS1seyZNDE3Lxr_R28v6qCaijrN1tyw8')
storage = MemoryStorage()
dp = Dispatcher(bot)

games = InlineKeyboardButton(text="games", callback_data="games")
yotube = InlineKeyboardButton(text="YouTube", callback_data="youtube")
instagram = InlineKeyboardButton(text="Instagram", callback_data="instagram")
yahoo = InlineKeyboardButton(text="Yahoo", callback_data="yahoo")
aol = InlineKeyboardButton(text="Aol", callback_data="aol")
gmail = InlineKeyboardButton(text="Gmail", callback_data="gmail")
hotmail = InlineKeyboardButton(text="Hotmail", callback_data="hotmail")
user = InlineKeyboardButton(text="User", callback_data="user")
list1 = InlineKeyboardButton(text="List", callback_data="list")
all_domin = InlineKeyboardButton(text="All Domin", callback_data="all_domin")
followers = InlineKeyboardButton(text="Followers", callback_data="followers")
following = InlineKeyboardButton(text="Following", callback_data="following")
back = InlineKeyboardButton(text="BACK", callback_data="back")
E = InlineKeyboardButton(text=f"DevLoper", url='https://t.me/ONCLIK')
info = InlineKeyboardButton(text="info", callback_data="info")
inst = InlineKeyboardMarkup(1).add(instagram,games,yotube,E)
list_insta = InlineKeyboardMarkup(1).add(info,user,yahoo,gmail,hotmail,aol,followers,following,E)
listG = InlineKeyboardMarkup(1).add(list1,all_domin,E) 
back1 = InlineKeyboardMarkup(1).add(back,E) 
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


@dp.message_handler(content_types=["text"])
async def process_start_command(message: types.Message):
	if '/info' in message.text:
				user = message.text.split('/info ')[1]
				headers = {'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36','viewport-width':'412','x-asbd-id':'198387','x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
				req = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=headers)
				if 'user' in req.text and 'data' in req.text:
					info = json.loads(req.content)['data']['user']
					username = info['username']
					id = info['id']
					name = info['full_name']
					bio = info['biography']
					post = info['edge_owner_to_timeline_media']['count']
					bio_link = info['bio_links']
					followers = info['edge_followed_by']['count']
					following = info['edge_follow']['count']
					isp = info['is_private']
					ver = info['is_verified']
					img = info['profile_pic_url']
					lok = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
					iok = lok.json()
					date = str(iok['date'])
					msge =(f'`🦍 INFO ᴵᴺˁᵀᴬᴳᴿᴬᴹ ᴮʸ ᴹᴼᴴᴬᴹᴹᴱᴰ ᴬᴸᴹᵁˁᵂᴵ⌯\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n🚹 ɴᴀᴍᴇ » {name}\n💡 ᴜsᴇʀɴᴀᴍᴇ » {username}\n🚻 ғᴏʟʟᴏᴡᴇʀs » {followers}\n🚸 ғᴏʟʟᴏᴡɪɴɢ » {following}\n📆 ᴅᴀᴛᴇ » {date}\n🗿 ɪᴅ » {id}\n📫 ᴘᴏsᴛs » {post}\n🗳️ ᴘʀɪvᴀᴛᴇ » {isp}\n📥 verified » {ver}\n📈 ʙɪᴏ » {bio}\n📽️ ʙɪᴏ LINK » {bio_link}\n📊 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n`')
					#bot.send_photo(me.chat.id,img,caption=msge,parse_mode = "markdown")
					await message.reply_photo(img,caption=msge,parse_mode="markdown")
					#await message.reply_video("https://scontent.cdninstagram.com/v/t66.30100-16/10000000_186386910715019_3997630578055552074_n.mp4?_nc_ht=instagram.fnjf8-2.fna.fbcdn.net&_nc_cat=111&_nc_ohc=DelwVbsK0iYAX_Aiwpb&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfCaEGUAQ__0b1Zo4klT4-CAxxxmhX8hmoCc616mJzEVAA&oe=63A28C2C&_nc_sid=8fd12b",caption="09")
					video = info['edge_owner_to_timeline_media']['edges']
					count = 0
					felix = 0
					text = 0
					while True:
						if 'video_url' in str(video[count]['node']):
							down = video[count]['node']['video_url']
							if 'text' in str(video[count]['node']['edge_media_to_caption']['edges'][0]):
								captionn = video[count]['node']['edge_media_to_caption']['edges'][text]['node']['text']
								await message.reply_video(down,caption=f"{captionn}")
								count+=1
							else:
								await message.reply_video(down,caption="*DOWNLOAD BY MOHAMMED ALMUSWI*",parse_mode="markdown")
								count+=1
						elif 'thumbnail_src' in str(video[count]['node']):
							down = video[count]['node']['thumbnail_src']
							if 'text' in str(video[count]['node']['edge_media_to_caption']['edges']):
								caption = video[count]['node']['edge_media_to_caption']['edges'][text]['node']['text']
								await message.reply_photo(down,caption=f"{caption}\nDOWNLOAD BY MOHAMMED ALMUSWI")
								count+=1
							else:
								await message.reply_photo(down,caption="*DOWNLOAD BY MOHAMMED ALMUSWI*",parse_mode="markdown")
								count+=1
						elif 'edge_felix_video_timeline' in info:
							infoo = info['edge_felix_video_timeline']['edges'][felix]['node']['video_url']
							await message.reply_video(infoo,caption="\n*DOWNLOAD BY MOHAMMED ALMUSWI*",parse_mode="markdown")
							felix+=1
	elif "/ip" in message.text:
		ip = message.text.replace('/ip ','')
		re = requests.get('https://ipinfo.io/widget/demo/{}'.format(ip),headers={'Host':'ipinfo.io','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-platform':'"Android"','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 10; YAL-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'*/*','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://ipinfo.io/?ip=151.236.167.108','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5'})
		if "Too Many Requests" in re.text or "Not Found" in re.text:
			await message.reply(str("❌"))
		else:
			req = re.json()
			ipA = req['data']['ip']
			city = req['data']['city']
			region = req['data']['region']
			country = req['data']['country']
			loc = req['data']['loc']
			org = req['data']['org']
			timezone = req['data']['timezone']
			asn = req['data']['asn']['asn']
			aname = req['data']['asn']['name']
			adomin = req['data']['asn']['domain']
			aro = req['data']['asn']['route']
			atype = req['data']['asn']['type']
			ncom = req['data']['company']['name']
			dcom = req['data']['company']['domain']
			tcom = req['data']['company']['type']
			crin = req['data']['carrier']['name']
			mcc = req['data']['carrier']['mcc']
			mnc = req['data']['carrier']['mnc']
			pvpn = req['data']['privacy']['vpn']
			pproxy = req['data']['privacy']['proxy']
			tor = req['data']['privacy']['tor']
			relay = req['data']['privacy']['relay']
			hosting = req['data']['privacy']['hosting']
			service = req['data']['privacy']['service']
			aab = req['data']['abuse']['address']
			cab = req['data']['abuse']['country']
			email = req['data']['abuse']['email']
			phone = req['data']['abuse']['phone']
			nab = req['data']['abuse']['name']
			network = req['data']['abuse']['network']
			domain = req['data']['domains']['total']
			aldom = req['data']['domains']['domains']
			Msge = (f"""
𝗗𝗮𝘁𝗮 : ☑️🌺 
𝗜𝗣 : *{ipA}* 
𝗖𝗜𝗧𝗬 : *{city}*
𝗥𝗘𝗚𝗜𝗢𝗡 : *{region}*
𝗖𝗢𝗨𝗡𝗧𝗥𝗬 : *{country}*
𝗟𝗢𝗖𝗔𝗟 : *{loc}*
𝗢𝗥𝗘𝗚𝗢𝗡 : *{org}*
𝗧𝗜𝗠𝗘𝗭𝗢𝗡𝗘 : *{timezone}*
𝗔𝗦𝗡 : *{asn}*
𝗔𝗦𝗡 𝗡𝗔𝗠𝗘 : *{aname}* 
𝗔𝗦𝗡 𝗗𝗢𝗠𝗜𝗡 : *{adomin}* 
𝗖𝗢𝗠𝗣𝗔𝗡𝗬 𝗡𝗔𝗠𝗘 : *{ncom}*
𝗖𝗢𝗠𝗣𝗔𝗡𝗬 𝗗𝗢𝗠𝗜𝗡 : *{dcom}*
𝗖𝗢𝗠𝗣𝗔𝗡𝗬 𝗧𝗬𝗣𝗘 : *{tcom}*
𝗖𝗔𝗥𝗥𝗜𝗘𝗥 𝗡𝗔𝗠𝗘 : *{crin}*
𝗠𝗖𝗖 : *{mcc}*
𝗠𝗡𝗖 : *{mnc}*
𝗩𝗣𝗡 : *{pvpn}*
𝗣𝗥𝗢𝗫𝗬 : *{pproxy}*
𝗛𝗢𝗦𝗧𝗜𝗡𝗚 : *{hosting}*
𝗧𝗢𝗥 : *{tor}*
𝗥𝗘𝗟𝗔𝗬 : *{relay}*
𝗦𝗘𝗥𝗩𝗜𝗖𝗘 : *{service}*
𝗔𝗕𝗨𝗦 𝗔𝗗𝗗𝗥𝗘𝗦𝗦 : *{aab}*
𝗔𝗕𝗨𝗦 𝗖𝗢𝗨𝗡𝗧𝗥𝗬 : *{cab}*
𝗔𝗕𝗨𝗦 𝗘𝗠𝗔𝗜𝗟 : *{email}* 
𝗔𝗕𝗨𝗦 𝗣𝗛𝗢𝗡𝗘 : *{phone}*
𝗔𝗕𝗨𝗦 𝗡𝗔𝗠𝗘 : *{nab}*
𝗧𝗢𝗧𝗔𝗟 𝗗𝗢𝗠𝗜𝗡𝗦 : *{domain}*
𝗗𝗢𝗠𝗜𝗡𝗦 : *{aldom}*
¶¬©𝐃𝐞𝐯𝐋𝐨𝐩𝐞𝐫 © 𝐁𝐲 𝐌𝐨𝐡𝐚𝐦𝐦𝐞𝐝 𝐀𝐥𝐦𝐮𝐬𝐰𝐢 ¶¬
""")
			await message.reply(Msge,parse_mode="markdown")
	elif "/bin" in message.text:
		try:
						frt = message.chat.first_name
						file = str(message.chat.username)+".txt"
						b = message.text.replace('/bin ','')
						with open(file, "a") as af:
							af.write(b)
						afi = open(file,"r").read().splitlines()
						for Bin in afi:
							Bin = Bin.split('\n')[0]
							u1=requests.get(f"https://api.dlyar-dev.tk/info-bin?bin={Bin}").json()
							bin = u1['bin']
							sc = u1['scheme']
							ty = u1['type']
							br = u1['brand']
							ba = u1['bank']
							co = u1['ccode']
							cu = u1['country']
							crr = u1['currency']
							fl = u1['flag']
							ph = u1['phone']
							msg = (f'𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ✅\n𝗕𝗜𝗡 ⇾ `{bin}`\n\n𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: `{sc} - {ty} - {br} - {ph}` \n𝗕𝗮𝗻𝗸: `{crr} - {ba}` \n𝗖𝗼𝘂𝗻𝘁𝗿𝘆: `{co} - {cu} - {fl}` \n𝗖𝗛𝗘𝗖𝗞 𝗕𝗬 : {frt}')
							await message.reply(msg,parse_mode="markdown")
						os.system("rm -rf "+str(file))
		except:
						await message.reply('Unavailable bin ❌')
	elif "/chk" in message.text:
		try:
						frt = message.chat.first_name
						file = str(message.chat.username)+".txt"
						b = message.text.replace('/chk ','')
						with open(file, "a") as af:
							af.write(b)
						afi = open(file,"r").read().splitlines()
						for Bin in afi:
							card = Bin.split('\n')[0]
							cc = card.split('|')[0]
							u1=requests.get(f"https://api.dlyar-dev.tk/info-bin?bin={cc}").json()
							bin = u1['bin']
							sc = u1['scheme']
							ty = u1['type']
							br = u1['brand']
							ba = u1['bank']
							co = u1['ccode']
							cu = u1['country']
							crr = u1['currency']
							fl = u1['flag']
							ph = u1['phone']
							url = requests.get(f'https://www.xchecker.cc/api.php?cc={card}').json()
							if url['details']=="Charge OK." and url['status']=="Live":
								msg = (f'''
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗖 ⇾ {card}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 1
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Approved  

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {sc} - {ty} - {br} - {ph} 
𝗕𝗮𝗻𝗸: {crr} - {ba} 
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {co} - {cu} - {fl}

𝗖𝗛𝗘𝗖𝗞 𝗕𝗬 : {frt}''')
								await message.reply(msg,parse_mode="markdown")
							elif url['details']=="Your card was declined." and url['status']=="Dead":
								msg = (f'''
𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌

𝗖𝗖 ⇾ {card}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 1
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Declined  

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {sc} - {ty} - {br} - {ph} 
𝗕𝗮𝗻𝗸: {crr} - {ba} 
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {co} - {cu} - {fl}

𝗖𝗛𝗘𝗖𝗞 𝗕𝗬 : {frt}''')
								await message.reply(msg,parse_mode="markdown")
						os.system("rm -rf "+str(file))
		except:
						await message.reply('BLACKLISTED_BIN: This BIN is blacklisted.')
	elif message.text == "/start":
		logo = 'https://t.me/{}'.format(message.chat.username)
		await message.reply_photo(logo,caption=("""
¶¬𝐇𝐢  : 𝐌𝐫. {}¶¬
¶¬𝐈𝐧𝐟𝐨 𝐂𝐡𝐚𝐭 : ¬>¶¬
¶¬𝐂𝐡𝐚𝐭 𝐈𝐝 : {}¶¬
¶¬𝐅𝐮𝐥𝐥 𝐍𝐚𝐦𝐞 : {}¶¬
¶¬𝐔𝐬𝐞𝐫𝐍𝐚𝐦𝐞  : @{}¶¬
¶¬𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐓𝐲𝐩𝐞: {}¶¬
¶¬©𝐃𝐞𝐯𝐋𝐨𝐩𝐞𝐫 © 𝐁𝐲 𝐌𝐨𝐡𝐚𝐦𝐦𝐞𝐝 𝐀𝐥𝐦𝐮𝐬𝐰𝐢 ¶¬""".format(message.chat.first_name,message.chat.id,message.chat.first_name,message.chat.username,message.chat.type)),reply_markup=inst)


@dp.callback_query_handler(text=["games", "youtube","instagram", "yahoo", "aol", "gmail", "hotmail", "user", "list", "all_domin", "followers", "following", "info","back"])
async def random(call: types.CallbackQuery):
	if call.data == "instagram":
		await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="menu", reply_markup=list_insta)	  
	if call.data == "info":
		await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="send me the comand /info + user instagram ",reply_markup=back1)	  
	if call.data == "back":
		await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="menu", reply_markup=list_insta)
	if call.data == "yahoo":
		await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="Yahoo start check hunter please wite.... ")
		ok=0;sk=0;bad=0;dom=0
		import random 
		while True:
			domin = '@hotmail.com'
			r = '1234567890'
			u = str("".join(random.choice(r)for i in range(5)))
			n0 = names.get_first_name(gender='male')
			n1 = names.get_first_name()
			n2 = names.get_first_name(gender='femal')
			pa2 = n0 + u 
			pa3 = n1 + u 
			pa4 = n2 + u
			ema = Faker().email().split("@")[0]
			em = (n0,n1,n2,ema,pa2,pa3,pa4)
			emil = random.choice(em)
			email = emil+domin
			user = email.split('@')[0]
			if (email.split('@')[1])=='hotmail.com':
				email = email
				user = user
				url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
				headers = {"Accept": "*/*","Content-Type": "application/x-www-form-urlencoded","User-Agent": str(generate_user_agent()),"Connection": "close","Host": "odc.officeapps.live.com","Accept-Encoding": "gzip, deflate","Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0","Accept-Language": "ar,en-US;q=0.9,en;q=0.8","canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c","uaid": "d06e1498e7ed4def9078bd46883f187b","Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
				data = ""
				response = requests.post(url, data=data, headers=headers)
				if ("Neither") in response.text:
					dom+=1
					url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
					headers = {'Host':'www.instagram.com','content-length':'66','sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"','x-ig-app-id':'1217981644879628','x-ig-www-claim':'0','sec-ch-ua-mobile':'?1','x-instagram-ajax':'1006732868','user-agent':'(Linux; Android 5.0; iPhone Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Mobile Safari/537.36','viewport-width':'424','content-type':'application/x-www-form-urlencoded','accept':'*/*','x-requested-with':'XMLHttpRequest','x-asbd-id':'198387','x-csrftoken':'wwuifuBVAerEMzq9tLsCA3sWcBv7zYMY','sec-ch-prefers-color-scheme':'light','sec-ch-ua-platform':'"Android"','origin':'https://www.instagram.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.instagram.com/accounts/password/reset/','accept-encoding':'gzip, deflate, br','accept-language':'en-IQ,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7,en-GB;q=0.6,en-US;q=0.5'}
					data = {"email_or_username":email,"recaptcha_challenge_field":""}
					req = requests.post(url, headers =headers, data =data).json()
					message = req['message']
					if 'No users found' ==message:
						bad+=1
					else:
						ok+=1
						headers = {'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36','viewport-width':'412','x-asbd-id':'198387','x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR1GMxGxYNiyJ_Qr59WPgznfqJKtnAogUcpBr_5hDMSoxwjz'}
						req = requests.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={user}",headers=headers)
						if not '<!DOCTYPE html>' in req.text:
									info = req.json()['data']['user']
									username = info['username']
									id = info['id']
									name = info['full_name']
									bio = info['biography']
									post = info['edge_owner_to_timeline_media']['count']
									bio_link = info['bio_links']
									followers = info['edge_followed_by']['count']
									following = info['edge_follow']['count']
									isp = info['is_private']
									ver = info['is_verified']
									img = info['profile_pic_url']
									lok = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
									iok = lok.json()
									date = str(iok['date'])
									hacker ="https://t.me/z9oon/13"
									msge = (f'`🦍 INFO ᴵᴺˁᵀᴬᴳᴿᴬᴹ ᴮʸ ᴹᴼᴴᴬᴹᴹᴱᴰ ᴬᴸᴹᵁˁᵂᴵ⌯\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n🚹 ɴᴀᴍᴇ » {name}\n💡 ᴜsᴇʀɴᴀᴍᴇ » {username}\nᴱᴹᴬᴵᴸ » {email}\n🚻 ғᴏʟʟᴏᴡᴇʀs » {followers}\n🚸 ғᴏʟʟᴏᴡɪɴɢ » {following}\n📆 ᴅᴀᴛᴇ » {date}\n🗿 ɪᴅ » {id}\n📫 ᴘᴏsᴛs » {post}\n🗳️ ᴘʀɪvᴀᴛᴇ » {isp}\n📥 verified » {ver}\n📈 ʙɪᴏ » {bio}\n📽️ ʙɪᴏ LINK » {bio_link}\n📊 𝙻𝙸𝙽𝚔 » https://www.instagram.com/{user}\n• ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ •\n`')
									await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=msge+'\nCOPY THE HITS SLEEP 20 SECONDS FOR REMOVE')
									sleep(20)
						elif '<!DOCTYPE html>' in req.text:
									await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=email+"\nLinked Instagram And Yahoo\nDev By *Mohammed Almuswi*"+'\nCOPY THE HITS SLEEP 20 SECONDS FOR REMOVE')
									sleep(20)
				else:
					sk+=1
					A = InlineKeyboardButton(text=f"erorr: {sk}", callback_data="games")
					B = InlineKeyboardButton(text=f"error insta: {bad}", callback_data="games")
					C = InlineKeyboardButton(text=f"Link Yahoo: {dom}", callback_data="games")
					O = InlineKeyboardButton(text=f"EMAIL: {email}", callback_data="games")
					D = InlineKeyboardButton(text=f"Success: {ok}", callback_data="games")
					E = InlineKeyboardButton(text=f"DevLoper", url='https://t.me/ONCLIK')
					erorr = InlineKeyboardMarkup(1).add(A, B, C, O, D, E) 
					await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='Consol dev By Mohammed Almuswi',reply_markup=erorr)
	elif call.data == "games":
		await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='click play button',reply_markup=InlineKeyboardMarkup(2).add(InlineKeyboardButton(text='play',web_app=WebAppInfo(url='https://poki.com/ar')),InlineKeyboardButton(text="BACK", callback_data="back"),InlineKeyboardButton(text=f"DevLoper", url='https://t.me/ONCLIK')))
		
	elif call.data == "youtube":
		await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption='click YouTube button',reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text='YouTube',web_app=WebAppInfo(url='https://www.youtube.com/'))))
		#await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="replace ", reply_markup=ky1)

executor.start_polling(dp,)
