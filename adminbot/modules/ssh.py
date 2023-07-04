from adminbot import *

@bot.on(events.CallbackQuery(data=b'delete-ssh'))
async def delete_ssh(event):
	async def delete_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond("**Username To Be Deleted:**")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
			cmd = f'printf "%s\n" "{user}" | delssh'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**User** `{user}` **Not Found**")
		else:
			await event.respond(f"**Successfully Deleted** `{user}`")
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
	async def create_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Password:**")
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
		cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" | addssh'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**⟨  SSH OVPN Account ⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username         :** `{user.strip()}`
**» Password         :** `{pw.strip()}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Host             :** `{DOMAIN}`
**» Port OpenSSH     :** `443, 80, 22`
**» Port Dropbear    :** `443, 109`
**» Port Dropbear WS :** `443, 109`
**» Port SSH WS      :** `80, 8080, 8081-9999 `
**» Port SSH SSL WS  :** `443`
**» Port SSL/TLS     :** `222-1000`
**» Port OVPN WS SSL :** `443`
**» Port OVPN SSL    :** `443`
**» Port OVPN TCP    :** `443, 1194`
**» Port OVPN UDP    :** `2200`
**» Port UDP Custom   :** `1-65535`
**» Proxy Squid      :** `3128`
**» BadVPN UDP       :** `7100, 7300, 7300`
**◇━━━━━━━━━━━━━━━━━◇**
**» Payload WSS      :** `GET wss://BUG.COM/ HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf][crlf]`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `{later}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'show-ssh'))
async def show_ssh(event):
	async def show_ssh_(event):
		cmd = 'bot-member-ssh'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""
```
{z}
```
**Show All SSH User**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await show_ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)



@bot.on(events.CallbackQuery(data=b'trial-ssh'))
async def trial_ssh(event):
	async def trial_ssh_(event):
		user = "trialX"+str(random.randint(100,1000))
		pw = "1"
		exp = "1"
		cmd = f'useradd -e `date -d "{exp} days" +"%Y-%m-%d"` -s /bin/false -M {user} && echo "{pw}\n{pw}" | passwd {user} | echo "killtrial ssh {user}" | at now +60 minutes &> /dev/null'
		try:
			subprocess.check_output(cmd,shell=True)
		except:
			await event.respond("**User Already Exist**")
		else:
			#today = DT.date.today()
			#later = today + DT.timedelta(days=int(exp))
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**⟨  SSH OVPN Account ⟩**
**◇━━━━━━━━━━━━━━━━━◇**
**» Username         :** `{user.strip()}`
**» Password         :** `{pw.strip()}`
**◇━━━━━━━━━━━━━━━━━◇**
**» Host             :** `{DOMAIN}`
**» Port OpenSSH     :** `443, 80, 22`
**» Port DNS         :** `443, 53 ,22`
**» Port Dropbear    :** `443, 109`
**» Port Dropbear WS :** `443, 109`
**» Port SSH WS      :** `80, 8080, 8081-9999 `
**» Port SSH SSL WS  :** `443`
**» Port SSL/TLS     :** `222-1000`
**» Port OVPN WS SSL :** `443`
**» Port OVPN SSL    :** `443`
**» Port OVPN TCP    :** `443, 1194`
**» Port OVPN UDP    :** `2200`
**» Port UDP Custom   :** `1-65535`
**» Proxy Squid      :** `3128`
**» BadVPN UDP       :** `7100, 7300, 7300`
**◇━━━━━━━━━━━━━━━━━◇**
**» Payload WSS      :** `GET wss://BUG.COM/ HTTP/1.1[crlf]Host: {DOMAIN}[crlf]Upgrade: websocket[crlf][crlf]`
**◇━━━━━━━━━━━━━━━━━◇**
**» Expired Until:** `60 Minutes`
**◇━━━━━━━━━━━━━━━━━◇**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'login-ssh'))
async def login_ssh(event):
	async def login_ssh_(event):
		cmd = 'bot-cek-login-ssh'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**shows logged in users SSH Ovpn**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
	async def ssh_(event):
		inline = [
[Button.inline(" TRIAL SSH ","trial-ssh"),
Button.inline(" CREATE SSH ","create-ssh")],
[Button.inline(" DELETE SSH ","delete-ssh"),
Button.inline(" CHECK Login SSH ","login-ssh")],
[Button.inline(" SHOW All USER SSH ","show-ssh")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**
**     ◇☘️⟨ SSH OVPN MANAGER ⟩☘️◇**
**◇━━━━━━━━━━━━━━━━━◇**
**» 🔰Service:** `SSH OVPN`
**» 🔰Hostname/IP:** `{DOMAIN}`
**» 🔰ISP:** `{z["isp"]}`
**» 🔰Country:** `{z["country"]}`
**◇━━━━━━━━━━━━━━━━━◇**
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)
