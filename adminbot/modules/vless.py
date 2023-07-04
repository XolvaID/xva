from adminbot import *

@bot.on(events.CallbackQuery(data=b'create-vless'))
async def create_vless(event):
	async def create_vless_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Quota:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline(" 3 Day ","3"),
Button.inline(" 7 Day ","7")],
[Button.inline(" 30 Day ","30"),
Button.inline(" 60 Day ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" | add-vless'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			x = [x.group() for x in re.finditer("vless://(.*)",a)]
			print(x)
			# remarks = re.search("#(.*)",x[0]).group(1)
			# domain = re.search("@(.*?):",x[0]).group(1)
			uuid = re.search("vless://(.*?)@",x[0]).group(1)
			# path = re.search("path=(.*)&",x[0]).group(1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ Xray/Vless Account ⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{user}`
**» Host Server :** `{DOMAIN}`
**» User Quota  :** `{pw} GB`
**» port TLS    :** `443-900`
**» Port NTLS   :** `80, 8080, 8081-9999`
**» NetWork     :** `(WS) or (gRPC)`
**» User ID     :** `{uuid}`
**» Path Vless  :** `vless `
**» Path Dynamic:** `http://BUG.COM/vless `
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS   : **
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link GRPC  :**
`{x[2].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'cek-vless'))
async def cek_vless(event):
	async def cek_vless_(event):
		cmd = 'bot-cek-vless'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**Shows Logged In Users Vless**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_vless_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
@bot.on(events.CallbackQuery(data=b'renew-vless'))
async def ren_vless(event):
	async def ren_vless_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline(" 3 Day ","3"),
Button.inline(" 7 Day ","7")],
[Button.inline(" 30 Day ","30"),
Button.inline(" 60 Day ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		cmd = f'printf "%s\n" "{user}" {exp} | renewvless'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""**Successfully Renewes {user} {exp} Days**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ren_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-vless'))
async def delete_vless(event):
	async def delete_vless_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | del-vless'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""**Successfully Deleted**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-vless'))
async def trial_vless(event):
	async def trial_vless_(event):
		async with bot.conversation(chat) as exp:
			cmd = f'printf "%s\n"| trialvless'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			#today = DT.date.today()
			#later = today + DT.timedelta(days=int(exp))
			x = [x.group() for x in re.finditer("vless://(.*)",a)]
			print(x)
			remarks = re.search("#(.*)",x[0]).group(1)
			# domain = re.search("@(.*?):",x[0]).group(1)
			uuid = re.search("vless://(.*?)@",x[0]).group(1)
			# path = re.search("path=(.*)&",x[0]).group(1)
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ Xray/Vless Account ⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Remarks     :** `{remarks}`
**» Host Server :** `{DOMAIN}`
**» Port DNS    :** `443, 53`
**» port TLS    :** `222-1000`
**» Port NTLS   :** `80, 8080, 8081-9999`
**» NetWork     :** `(WS) or (gRPC)`
**» User ID     :** `{uuid}`
**» Path Vless  :** `/vless `
**» Path Dynamic:** `http://BUG.COM/vless `
**◇━━━━━━━━━━━━━━━━━◇**
**» Link TLS   : **
`{x[0]}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link NTLS  :**
`{x[1].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Link GRPC  :**
`{x[2].replace(" ","")}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until :** `60 Minutes`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_vless_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'vless'))
async def vless(event):
	async def vless_(event):
		inline = [
[Button.inline(" TRIAL VLESS ","trial-vless"),
Button.inline(" CREATE VLESS ","create-vless")],
[Button.inline(" CHECK VLESS ","cek-vless"),
Button.inline(" DELETE VLESS ","delete-vless")],
[Button.inline(" RENEW VLESS ","renew-vless")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**     ◇☘️⟨ VLESS MANAGER ⟩☘️◇**
**◇━━━━━━━━━━━━━━━━━◇**
** 🔰 Service:** `VLESS`
** 🔰 Hostname/IP:** `{DOMAIN}`
** 🔰 ISP:** `{z["isp"]}`
** 🔰 Country:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await vless_(event)
	else:
		await event.answer("Access Denied",alert=True)
