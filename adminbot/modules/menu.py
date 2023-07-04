from adminbot import *

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline(" SSH OVPN MANAGER ","ssh")],
[Button.inline(" VMESS MANAGER ","vmess"),
Button.inline(" VLESS MANAGER ","vless")],
[Button.inline(" TROJAN MANAGER ","trojan")],
[Button.inline(" OTHER SETTING ","setting")]]
	ox = requests.get(f"https://ipv4.icanhazip.com").text.strip()
	bz = f" curl -sS https://github.com/XolvaID/ip | grep '{ox}'| cut -d ' ' -f6 "
	bo = subprocess.check_output(bz, shell=True).decode("ascii").strip()
	if not ox != bo:
		sender = await event.get_sender()
		val = valid(str(sender.id))
		if val == "false":
			try:
				await event.answer("Akses Ditolak", alert=True)
			except:
				await event.reply("Akses Ditolak")
		elif val == "true":
			sh = f' cat /etc/ssh/.ssh.db | grep "###" | wc -l'
			ssh = subprocess.check_output(sh, shell=True).decode("ascii")
			vm = f' cat /etc/vmess/.vmess.db | grep "###" | wc -l'
			vms = subprocess.check_output(vm, shell=True).decode("ascii")
			vl = f' cat /etc/vless/.vless.db | grep "###" | wc -l'
			vls = subprocess.check_output(vl, shell=True).decode("ascii")
			tr = f' cat /etc/trojan/.trojan.db | grep "###" | wc -l'
			trj = subprocess.check_output(tr, shell=True).decode("ascii")
			hap = subprocess.call(["systemctl", "is-active", "--quiet", "haproxy"])
			if(hap == 0):
				hap1 = f'🟢'
			else:
				hap1 = f'🔴'
			ngx = subprocess.call(["systemctl", "is-active", "--quiet", "nginx"])
			if(ngx == 0):
				ngx1 = f'🟢'
			else:
				ngx1 = f'🔴'
			xr = subprocess.call(["systemctl", "is-active", "--quiet", "xray"])
			if(xr == 0):
				xr1 = f'🟢'
			else:
				xr1 - f'🔴'
			sh = subprocess.call(["systemctl", "is-active", "--quiet", "ws"])
			if(sh == 0):
				ws1 = f'🟢'
			else:
				ws1 = f'🔴'
			msg = f"""
**◇━━━━━━━━━━━━━━━━━◇**,
**  ◇☘️ ADMIN PANEL BOT ☘️◇**
**◇━━━━━━━━━━━━━━━━━◇**
**          --~~ Service Status~~--**
**  HAPROXY  :**  `{hap1}`  ** XRAY         :**  `{xr1}`
**  NGINX         :**  `{ngx1}` **  WS EPRO :**  `{ws1}`

**      --~~Total Account Created~~--** 
** 🥱 SSH OVPN    :** `{ssh.strip()}` 
** 🙄 XRAY VMESS  :** `{vms.strip()}` 
** 😬 XRAY VLESS  :** `{vls.strip()}` 
** 🤑 XRAY TROJAN :** `{trj.strip()}` 
**◇━━━━━━━━━━━━━━━━━◇**
"""
			x = await event.edit(msg,buttons=inline)
			if not x:
				await event.reply(msg,buttons=inline)
	else:
		await event.respond(f"** You Dont Have Access**")


