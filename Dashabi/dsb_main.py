import requests
import os
import re
import json
import time
import random
import timeit
import urllib
from datetime import datetime
from dateutil import tz


   
   
result=''
osenviron={}
hd={}
urllist=[]
hdlist=[]
btlist=[]
bdlist=[]
SB=''
SP=0

djj_bark_cookie=''
djj_sever_jiang=''
djj_tele_cookie=''

def Av(i,hd,k,key=''):
   print(str(k)+'=🔔='*k)
   try:
     if k==1:
       key=bdlist[0]
     if k==8:
       key=bdlist[2]
     if k==16:
       key=bdlist[3]
     if k==18:
       key=bdlist[4]
     if k==19:
       key=bdlist[5]
     response =requests.post(i,headers=hd,data=key,timeout=10)
     userRes=json.loads(response.text)
     #print(userRes)
     hand(userRes,k)

   except Exception as e:
      print(str(e))


def hand(userRes,k):
  global SB,SP
  try:
   if k==1:
     for mm in userRes:
      if mm['is_ok']==0:
         Av(urllist[k],hd,k+1,'mini_id='+mm['mini_id']+'&')
      else:
        print('completed......')
   if k==2:
     SB='taskid='+str(userRes['taskid'])+'&nonce_str='+userRes['nonce_str']+'&'
     print(userRes['nonce_str'])
     time.sleep(30)
     Av(urllist[k],hd,k+1,SB)
   if k==3:
     #print(userRes['msg'])
     if userRes['code']==1:
       print(f'''rd2:{userRes['jinbi']}''')
       bd=bdlist[1]+userRes['fb_str']
       Av(urllist[k],hd,k+1,bd)
     else:
        #print(userRes['msg'])
        if json.dumps(userRes).find('u8fc7')>0:
          time.sleep(10) 
          Av(urllist[k-1],hd,k,SB)
   if k==4:
       print('fb:'+userRes['msg'])
   if k==5:
        print('card:'+str(userRes['ka']))
        if userRes['ka']==0:
          return 
        for p in userRes['list']:
          if p['is_ad']=='0':
            bd='gid='+p['id']+'&'
            print(bd)
            Av(urllist[k],hd,k+1,bd)
            time.sleep(5)
   if k==6:
         bd='sign='+userRes['sign']+'&gid='+userRes['id']+'&glid='+str(userRes['glid'])+'&'
         Av(urllist[k],hd,k+1,bd)
   if k==7:
        print(f'''jf:{userRes['jf']}-{userRes['up']}''')
        time.sleep(15)
        Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==8:
       
       if userRes['code']==1:
         print(f'''rd:{userRes['jinbi']}_{userRes['nonce_str']}''')
         time.sleep(10)
         Av(urllist[k],hd,k+1,'nonce_str='+userRes['nonce_str']+'&')
   if k==9:
      if userRes['code']==-1:
          print(userRes['msg'])
      elif userRes['code']==1:
        print(f'''JB:{userRes['day_jinbi']}_{userRes['jinbi']}''')
        SP+=1
        if SP<random.randint(10,20):
          Av(urllist[k-2],hd,k-1)
   if k==10:
     if userRes['code']==1:
       print('已转'+str(userRes['lucky_count'])+'次,剩余:'+str(userRes['lucky_num'])+'次,获得'+str(userRes['jinbi'])+'金币')
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
       if userRes['lucky_num']>0:
          time.sleep(10)
          Av(urllist[k-1],hd,k)
     else:
           print(userRes['msg'])
           for x in range(1,5):
             Av(urllist[k],hd,k+1,'box='+str(x)+'&')
             time.sleep(1)
   if k==11:
      if userRes['code']==-1:
       print(userRes['msg'])
      elif userRes['code']==1:
        Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==12:
      print(userRes)
      msg='Red:'+str(userRes['idx_hongbao_num'])+'|'
      print(msg)
      
      if userRes['steps_btn']!="明天再领":
        Av(urllist[14],hd,15)
      if userRes['jindan_show']==0:
          Av(urllist[12],hd,13)
      if userRes['hb_time']<=0:
         Av(urllist[15],hd,16)
      if userRes['right_jinbi']!='160':
         Av(urllist[16],hd,17)
      if userRes['right_jinbi']=='160':
         Av(urllist[17],hd,18)
         time.sleep(2)
         Av(urllist[18],hd,19)
   if k==13:
     if userRes['code']==-1:
       print(userRes['msg'])
     elif userRes['code']==1:
      print('JDDD:'+str(userRes['code']))
      bd='taskid='+str(userRes['taskid'])+'&clicktime=1611232580&donetime=1611232583&nonce_str='+userRes['nonce_str']+'&'
      Av(urllist[k],hd,k+1,bd)
   if k==14:
     if userRes['code']==-1:
       print(userRes)
     elif userRes['code']==1:
       print('JB'+str(userRes['jinbi']))
       time.sleep(5)
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
       time.sleep(10)
       print(urllist[k-2])
       Av(urllist[k-2],hd,k-1)
   if k==15:
     if userRes['code']==-1:
        print(userRes['msg']+'HB,completed......')
     elif userRes['code']==1:
       print(f'''{userRes['msg']},HB_JB:{userRes['jinbi']}''')
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==16:
     if userRes['code']==-1:
        print(userRes['msg']+'RED:,completed......')
     elif userRes['code']==1:
       print('red:'+userRes['nonce_str'])
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==17:
     if userRes['code']==-1:
        print(userRes['msg']+'homeJB1,completed......')
     elif userRes['code']==1:
       print('homeJB1:'+userRes['jinbi']+','+userRes['msg'])
       Av(urllist[3],hd,4,bdlist[1]+userRes['nonce_str'])
   if k==18:
      print(userRes)
   if k==19:
     if userRes['code']==-1:
        print(userRes['msg']+'homeJB2,completed......')
     elif userRes['code']==1:
       print('homeJB2:'+userRes['jinbi']+','+userRes['msg'])
  except Exception as e:
      print(str(e))



def watch(flag,list):
   vip=''
   global djj_bark_cookie
   global djj_sever_jiang
   global djj_tele_cookie
   if "DJJ_BARK_COOKIE" in os.environ:
      djj_bark_cookie = os.environ["DJJ_BARK_COOKIE"]
   if "DJJ_TELE_COOKIE" in os.environ:
      djj_tele_cookie = os.environ["DJJ_TELE_COOKIE"]
   if "DJJ_SEVER_JIANG" in os.environ:
      djj_sever_jiang = os.environ["DJJ_SEVER_JIANG"]
   if flag in os.environ:
      vip = os.environ[flag]
   if flag in osenviron:
      vip = osenviron[flag]
   if vip:
       for line in vip.split('\n'):
         if not line:
            continue 
         list.append(line.strip())
       return list
   else:
       print(f'''【{flag}】 is empty,DTask is over.''')
      # exit()

def clock(func):
    def clocked(*args, **kwargs):
        t0 = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[🔔运行完毕用时%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked
    
@clock
def start():
  global result,hd,bdlist,urllist,hdlist
  try:
   print('Localtime',datetime.now(tz=tz.gettz('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S", ))
   watch('dashabi_main_url',urllist)
   watch('dashabi_hd',hdlist)
   watch('dashabi_bd',bdlist)
   if len(urllist)==0 or len(hdlist)==0:
      print('data is null.......')
      exit()
   
   for loop in range(1):
    for c in range(len(hdlist)):
      hd=eval(hdlist[c])
      print('【'+str(loop+1)+'】C:'+str(c+1))
      for u in range(len(urllist)):
        if u==0 or u==4 or u==7 or u==9 or u==11:
          Av(urllist[u],hd,u+1)
        else:
          continue
  except Exception as e:
      print(str(e))
  print('🏆🏆🏆🏆运行完毕')
  
    
    
   
     
if __name__ == '__main__':
       start()
    
