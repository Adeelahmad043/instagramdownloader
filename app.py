from flask import Flask, render_template, request, url_for, redirect, send_file, session
import requests
import os, shutil
import instaloader
import youtube_dl
app = Flask(__name__)
app.config['SECRET_KEY'] = "654c0fb3968af9d5e6a9b3edcbc7051b"




@app.route("/", methods = ["GET", "POST"])
def home():

	if request.method == "POST":
		try:
			
			
			url = request.form["url"]
			url = url.replace("?utm_source=ig_web_copy_link", "")
			session['link'] = url
			url_pl = f"{url}embed/"
			urls = url_pl.replace("embed/", "?__a=1")
			headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
			response = requests.get(url=urls, headers=headers)
			r = response.json()
			username = r['graphql']['shortcode_media']["owner"]["username"]
			url = "https://www.instagram.com/"+username+"/"+"?__a=1"
			response = requests.get(url=url, headers=headers)
			r = response.json()
			biography = r['graphql']['user']["biography"]
			followers = r['graphql']['user']["edge_followed_by"]["count"]
			following = r['graphql']['user']["edge_follow"]["count"]
			fullname = r['graphql']['user']["full_name"]
			post = r['graphql']['user']["edge_owner_to_timeline_media"]["count"]
		except:
			return render_template("pikerror.html")
		return render_template("download.html", url=url_pl, username=username, post=post, fullname=fullname, following=following, followers=followers, biography=biography)
	return render_template("pik_download.html")
@app.route("/download", methods = ["GET", "POST"])
def download_photo():
	url = session['link']
	url = url.replace("?utm_source=ig_web_copy_link", "")
	url = f"{url}?__a=1"
    
	headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    
	response = requests.get(url=url, headers=headers)

	if response.ok:

		r = response.json()
		pic_url = (r['graphql']['shortcode_media']['display_url'])
	return redirect(pic_url+"&dl=1")

@app.route('/vide_download', methods = ["GET", "POST"])
def vide_download():
	if request.method == "POST":
		
		try:
			url = request.form["url"]
			url = url.replace("?utm_source=ig_web_copy_link", "")
			session['link'] = url
			url_pl = f"{url}embed/"
			urls = url_pl.replace("embed/", "?__a=1")
			headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
			response = requests.get(url=urls, headers=headers)
			r = response.json()
			username = r['graphql']['shortcode_media']["owner"]["username"]
			url = "https://www.instagram.com/"+username+"/"+"?__a=1"
			response = requests.get(url=url, headers=headers)
			r = response.json()
			biography = r['graphql']['user']["biography"]
			followers = r['graphql']['user']["edge_followed_by"]["count"]
			following = r['graphql']['user']["edge_follow"]["count"]
			fullname = r['graphql']['user']["full_name"]
			post = r['graphql']['user']["edge_owner_to_timeline_media"]["count"]
		except:
			return render_template("videoerror.html")
		return render_template("download_1.html", url=url_pl, username=username, post=post, fullname=fullname, following=following, followers=followers, biography=biography)
	return render_template("video_download.html")


@app.route("/download_1", methods = ["GET", "POST"])
def video_download():
	url = session['link']
	url = url.replace("?utm_source=ig_web_copy_link", "")
	try:
		with youtube_dl.YoutubeDL() as ydl:
			url = ydl.extract_info(url, download=False)
			try:
				download_link = url["entries"][-1]["formats"][-1]["url"]
			except:
				download_link = url["formats"][-1]["url"]
		return redirect(download_link+"&dl=1")
	except:
		return render_template("error.html")

@app.route('/story')
def sotri():
	return render_template('story.html')

@app.route('/storydownload', methods=["POST", "GET"])
def storydownload():

	if request.method == "POST":
		try:
			insta = instaloader.Instaloader()
			idname = 'adeelahmad043@gmail.com'
			password = 'Yahoo.44'
			insta.login(idname,password)
			username = request.form["url"]
			if os.path.exists(f'static/{username}'):
				shutil.rmtree(f'static/{username}')
			shutil.move(username,'static')
			imglist = os.listdir(f'static/{username}')
			for i in imglist:
				if 'UTC_profile_pic.jpg'  in i:
					os.unlink( f'static/{username}/{i}')
				if '.json' in i:
					os.unlink(f'static/{username}/{i}')
				if 'id' in i:
					os.unlink(f'static/{username}/{i}')
				if 'profile_pik' in i:
					os.unlink(f'static/{username}/{i}')
				imglist = os.listdir(f'static/{username}')
		except:
			return render_template("sterror.html")
		return render_template("storydownload.html", imagelist=imglist, username=username)
	return render_template("storydownload.html")

@app.route('/igtv_download', methods=["POST", "GET"])
def igtv_download():
	if request.method == "POST":
		try:
			url = request.form["url"]
			url = url.replace("?utm_source=ig_web_copy_link", "")
			session['link'] = url
			url_pl = f"{url}embed/"
			urls = url_pl.replace("embed/", "?__a=1")
			headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
			response = requests.get(url=urls, headers=headers)
			r = response.json()
			username = r['graphql']['shortcode_media']["owner"]["username"]
			url = "https://www.instagram.com/"+username+"/"+"?__a=1"
			response = requests.get(url=url, headers=headers)
			r = response.json()
			biography = r['graphql']['user']["biography"]
			followers = r['graphql']['user']["edge_followed_by"]["count"]
			following = r['graphql']['user']["edge_follow"]["count"]
			fullname = r['graphql']['user']["full_name"]
			post = r['graphql']['user']["edge_owner_to_timeline_media"]["count"]
		except:
			return render_template("igtverror.html")
		return render_template("download_igtv.html", url=url_pl, username=username, post=post, fullname=fullname, following=following, followers=followers, biography=biography)
	return render_template("igtv_download.html")

@app.route('/dp_download')
def dp_download():
	return render_template('dp_download.html')

@app.route('/download_DP', methods=["POST", "GET"])
def download_DP():
	if request.method == "POST":
		try:
			url = request.form["url"]
			# print("Someone just tried to download", url)
    
			# username = url.lower()
        
			url = f"https://www.instagram.com/{url}/?__a=1"
        
			headers = {
				'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
			}
        
			response = requests.get(url=url, headers=headers)
        
			if response.ok:
            
				r = response.json()
				pic_url = r['graphql']['user']['profile_pic_url_hd']
			return redirect(pic_url+"&dl=1")
		except:
			return render_template("Dperror.html")
	return render_template("dp_download.html")
	
@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/terms-conditions')
def terms():
	return render_template('terms-conditions.html')		
	
if __name__ == '__main__':
	app.run(port=80, debug=True)




