# -*- coding: utf-8 -*-
# 康虎软件工作室
# http://www.khcloud.net
# QQ: 360026606
# wechat: 360026606
#--------------------------
if 64 - 64: i11iIiiIii
import os
import sys
import logging
import string
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
try :
 import simplejson as json
except ImportError :
 import json
import time
if 73 - 73: II111iiii
try :
 import xml . etree . cElementTree as ET
except ImportError :
 import xml . etree . ElementTree as ET
from xml . dom import minidom
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
from odoo . exceptions import AccessError , UserError , ValidationError
from odoo import models , fields , api , _
try :
 from Crypto . Util . Padding import pad , unpad
 from Crypto . Cipher import AES
except ImportError as I1IiI :
 raise ImportError ( 'Failed to load module Crypto! Please install pycryptodome first!' )
 if 73 - 73: OOooOOo / ii11ii1ii
O00ooOO = logging . getLogger ( __name__ )
if 47 - 47: oO0ooO % iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
if 68 - 68: o00ooo0 / oO0o0ooO0
import os
import sys
import hashlib
import string
import random
import base64
from binascii import b2a_hex , a2b_hex
if 88 - 88: ii1II11I1ii1I . OOooOOo % o00ooo0
from Crypto import Random
from Crypto . Cipher import AES
if 66 - 66: ii1II11I1ii1I
IiiiIiI1iIiI1 = ( 'C' )
ooo0Oo0 = ( 'FS' )
oo = ( 'O' )
O0Oooo00 = ( 'F' )
Ooo0 = ( 'T' )
oo00000o0 = ( 'S' )
if 34 - 34: oO0o0ooO0 % II111iiii % iIii1I11I1II1 % oO0o0ooO0 * ii1II11I1ii1I / OoOoOO00
Iiii = ( 't' )
OOO0O = ( 'u' )
oo0ooO0oOOOOo = ( 'd' )
oO000OoOoo00o = ( 'i' )
iiiI11 = ( 'o72' )
OOooO = ( '0' )
OOoO00o = ( '1' )
if 9 - 9: I1IiiI - iI1Ii11111iIi % i1IIi % OoooooooOO
i1iIIi1 = b'1234567890123456'
if 50 - 50: i11iIiiIii - iI1Ii11111iIi
def oo0Ooo0 ( ) :
 return '' . join ( IiiiIiI1iIiI1 + ooo0Oo0 + oo + O0Oooo00 + Ooo0 + oo00000o0 + Iiii + OOO0O + oo0ooO0oOOOOo + oO000OoOoo00o + iiiI11 + OOooO + OOoO00o )
 if 46 - 46: o00ooo0 % o00ooo0 - OOooOOo * o0oOOo0O0Ooo % ii1II11I1ii1I
 if 55 - 55: OoOoOO00 % i1IIi / iI1Ii11111iIi - OOooOOo - O0 / II111iiii
iii11iII = len ( oo0Ooo0 ( ) )
i1I111I = lambda i11I1IIiiIi : i11I1IIiiIi + ( iii11iII - len ( i11I1IIiiIi ) % iii11iII ) * chr ( iii11iII - len ( i11I1IIiiIi ) % iii11iII )
IiIiIi = lambda i11I1IIiiIi : i11I1IIiiIi [ 0 : - ord ( i11I1IIiiIi [ - 1 ] ) ]
if 40 - 40: OOooOOo . OoOoOO00 . Oo0Ooo . i1IIi
class I11iii ( object ) :
 def __init__ ( self , key = False , mode = AES . MODE_CBC ) :
  if 54 - 54: ii11ii1ii + ii11ii1ii % iiIIIII1i1iI % i11iIiiIii / iIii1I11I1II1 . ii11ii1ii
  if 57 - 57: iI1Ii11111iIi % OoooooooOO
  if 61 - 61: ii1II11I1ii1I . iIii1I11I1II1 * I1IiiI . o00ooo0 % Oo0Ooo
  if 72 - 72: ii11ii1ii
  if 63 - 63: iI1Ii11111iIi
  if 86 - 86: o00ooo0 . I1IiiI % Oo0Ooo + o0oOOo0O0Ooo
  if 35 - 35: iIii1I11I1II1 % OOooOOo * oO0ooO % oO0ooO + II111iiii * ii1II11I1ii1I
  if 54 - 54: oO0ooO + oO0o0ooO0 / ii1II11I1ii1I
  if 9 - 9: OoOoOO00 / Oo0Ooo - oO0o0ooO0 . i1IIi / I1IiiI % oO0o0ooO0
  if 71 - 71: iiIIIII1i1iI . O0
  if 73 - 73: ii11ii1ii % OoOoOO00 - iI1Ii11111iIi
  if 10 - 10: I1IiiI % I1ii11iIi11i
  if 48 - 48: oO0ooO + oO0ooO / II111iiii / iIii1I11I1II1
  if 20 - 20: o0oOOo0O0Ooo
  self . key = key or oo0Ooo0 ( )
  self . mode = mode
  self . key = self . key . encode ( 'utf-8' )
  if 77 - 77: OoOoOO00 / oO0ooO
 @ staticmethod
 def get_machine_code ( ) :
  import uuid
  if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / o0oOOo0O0Ooo
  return str ( uuid . UUID ( int = uuid . getnode ( ) ) )
  if 28 - 28: ii11ii1ii - oO0o0ooO0 . oO0o0ooO0 + OoOoOO00 - OoooooooOO + O0
 @ staticmethod
 def rand_aes_key ( size = 16 , by_base64 = True , chars = string . ascii_uppercase + string . digits ) :
  oOoOooOo0o0 = '' . join ( random . choice ( chars ) for _ in range ( size ) )
  if 61 - 61: o0oOOo0O0Ooo / OoO0O00 + o00ooo0 * OOooOOo / OOooOOo
  if 75 - 75: i1IIi / OoooooooOO - O0 / OoOoOO00 . II111iiii - i1IIi
  if 71 - 71: ii11ii1ii + iI1Ii11111iIi * ii11ii1ii - OoO0O00 * o0oOOo0O0Ooo
  if 65 - 65: O0 % I1IiiI . I1ii11iIi11i % iIii1I11I1II1 / ii11ii1ii % iiIIIII1i1iI
  if 51 - 51: i11iIiiIii . I1IiiI + II111iiii
  if 10 - 10: I1ii11iIi11i * o00ooo0 * II111iiii % iI1Ii11111iIi . ii11ii1ii + iiIIIII1i1iI
  return base64 . b64encode ( oOoOooOo0o0 ) if by_base64 else oOoOooOo0o0
  if 19 - 19: OoOoOO00 - I1IiiI . ii11ii1ii / oO0o0ooO0
  if 33 - 33: iiIIIII1i1iI / I1ii11iIi11i % I1IiiI + o00ooo0 / OoO0O00
 def encrypt ( self , text ) :
  if 52 - 52: o0oOOo0O0Ooo - OoooooooOO + iI1Ii11111iIi + iI1Ii11111iIi - o0oOOo0O0Ooo / iiIIIII1i1iI
  text = pad ( text . encode ( 'utf-8' ) , block_size = 16 )
  I1I = i1iIIi1
  if type ( i1iIIi1 ) == 'str' :
   I1I = i1iIIi1 . encode ( "utf8" )
   if 24 - 24: I1ii11iIi11i
  o0Oo0O0Oo00oO = AES . new ( self . key , self . mode , i1iIIi1 )
  if 39 - 39: oO0o0ooO0 - II111iiii * OoO0O00 % o0oOOo0O0Ooo * II111iiii % II111iiii
  self . ciphertext = o0Oo0O0Oo00oO . encrypt ( text )
  if 59 - 59: iIii1I11I1II1 + I1IiiI - o0oOOo0O0Ooo - I1IiiI + ii11ii1ii / I1ii11iIi11i
  return base64 . b64encode ( self . ciphertext )
  if 24 - 24: oO0ooO . ii1II11I1ii1I % ii11ii1ii + o00ooo0 % OoOoOO00
  if 4 - 4: oO0o0ooO0 - OoO0O00 * OoOoOO00 - oO0ooO
 def decrypt ( self , text ) :
  II1 = base64 . b64decode ( text )
  o0Oo0O0Oo00oO = AES . new ( self . key , self . mode , i1iIIi1 )
  if 34 - 34: oO0o0ooO0 - oO0o0ooO0 * I1IiiI + iI1Ii11111iIi % oO0o0ooO0
  if 4 - 4: OOooOOo
  if 93 - 93: OoO0O00 % OOooOOo . OoO0O00 * iiIIIII1i1iI % iI1Ii11111iIi . II111iiii
  if 38 - 38: o0oOOo0O0Ooo
  if 57 - 57: O0 / OOooOOo * iiIIIII1i1iI / OoOoOO00 . II111iiii
  if 26 - 26: ii1II11I1ii1I
  OOO = bytes . decode ( unpad ( o0Oo0O0Oo00oO . decrypt ( II1 ) , block_size = 16 ) )
  return OOO
  if 59 - 59: II111iiii + OoooooooOO * OoOoOO00 + i1IIi
  if 58 - 58: II111iiii * ii11ii1ii * I1ii11iIi11i / ii11ii1ii
from Crypto import Random
from Crypto . Hash import SHA
from Crypto . Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto . Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto . PublicKey import RSA
if 75 - 75: OOooOOo
class I1III ( ) :
 if 63 - 63: ii11ii1ii % OOooOOo * OOooOOo * OoO0O00 / I1ii11iIi11i
 if 74 - 74: II111iiii
 if 75 - 75: o0oOOo0O0Ooo . o00ooo0
 if 54 - 54: II111iiii % OoOoOO00 % oO0ooO % iIii1I11I1II1 + iIii1I11I1II1 * o00ooo0
 if 87 - 87: o00ooo0 * Oo0Ooo % i11iIiiIii % OoOoOO00 - ii11ii1ii
 if 68 - 68: iiIIIII1i1iI % i1IIi . oO0o0ooO0 . I1ii11iIi11i
 if 92 - 92: ii1II11I1ii1I . iiIIIII1i1iI
 if 31 - 31: iiIIIII1i1iI . OoOoOO00 / O0
 if 89 - 89: OoOoOO00
 if 68 - 68: OoO0O00 * OoooooooOO % O0 + OoO0O00 + o00ooo0
 if 4 - 4: o00ooo0 + O0 * ii11ii1ii
 if 55 - 55: Oo0Ooo + iIii1I11I1II1 / OoOoOO00 * OOooOOo - i11iIiiIii - iI1Ii11111iIi
 if 25 - 25: I1ii11iIi11i
 if 7 - 7: i1IIi / I1IiiI * iiIIIII1i1iI . oO0o0ooO0 . iIii1I11I1II1
 if 13 - 13: ii11ii1ii / i11iIiiIii
 def __init__ ( self , pri_key = 'pri.pem' , pub_key = 'pub.pem' , key_path = os . path . abspath ( os . path . dirname ( __file__ ) ) ) :
  self . KEY_PRIVATE = pri_key
  self . KEY_PUBLIC = pub_key
  self . KEY_PATH = key_path
  if 2 - 2: I1IiiI / O0 / o0oOOo0O0Ooo % OoOoOO00 % iI1Ii11111iIi
 def gen_key_pair ( self ) :
  if 52 - 52: o0oOOo0O0Ooo
  o0OO0oOO0O0 = Random . new ( ) . read
  if 8 - 8: OOooOOo
  iIi1IIIi1 = RSA . generate ( 1024 , o0OO0oOO0O0 )
  if 86 - 86: oO0ooO % OoOoOO00 / I1IiiI / OoOoOO00
  if 42 - 42: OoO0O00
  o0o = iIi1IIIi1 . exportKey ( )
  if 84 - 84: O0
  with open ( self . KEY_PATH + "/" + self . KEY_PRIVATE , 'w' ) as OOOooOO0 :
   OOOooOO0 . write ( o0o )
   if 87 - 87: OOooOOo * I1ii11iIi11i + ii11ii1ii / iIii1I11I1II1 / ii1II11I1ii1I
  I1111IIi = iIi1IIIi1 . publickey ( ) . exportKey ( )
  with open ( self . KEY_PATH + "/" + self . KEY_PUBLIC , 'w' ) as OOOooOO0 :
   OOOooOO0 . write ( I1111IIi )
   if 93 - 93: OoooooooOO / I1IiiI % i11iIiiIii + I1ii11iIi11i * OoO0O00
 def decrypt_str ( self , encrypt_text ) :
  if 15 - 15: oO0ooO . OoO0O00 / Oo0Ooo + oO0ooO
  Ooo = self . KEY_PATH + "/" + self . KEY_PUBLIC
  if not os . path . isfile ( Ooo ) :
   raise Exception ( "Decrypt key not exist or invalid!" )
   if 62 - 62: ii11ii1ii / OoO0O00 + iI1Ii11111iIi / OoO0O00 . II111iiii
  o0OO0oOO0O0 = Random . new ( ) . read
  with open ( self . KEY_PATH + "/" + self . KEY_PRIVATE ) as OOOooOO0 :
   ooOOoooooo = OOOooOO0 . read ( )
   II1I = RSA . importKey ( ooOOoooooo )
   O0i1II1Iiii1I11 = Cipher_pkcs1_v1_5 . new ( II1I )
   OOO = O0i1II1Iiii1I11 . decrypt ( base64 . b64decode ( encrypt_text ) , o0OO0oOO0O0 )
   return OOO
   if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
 def encrypt_str ( self , message ) :
  Ooo = self . KEY_PATH + "/" + self . KEY_PUBLIC
  if not os . path . isfile ( Ooo ) :
   raise Exception ( "Encrypt key not exist or invalid!" )
   if 91 - 91: ii1II11I1ii1I % i1IIi % iIii1I11I1II1
  with open ( Ooo ) as OOOooOO0 :
   ooOOoooooo = OOOooOO0 . read ( )
   II1I = RSA . importKey ( ooOOoooooo )
   O0i1II1Iiii1I11 = Cipher_pkcs1_v1_5 . new ( II1I )
   IIi1I11I1II = base64 . b64encode ( O0i1II1Iiii1I11 . encrypt ( message ) )
   return IIi1I11I1II
   if 63 - 63: OoooooooOO - OoO0O00 . II111iiii / o0oOOo0O0Ooo . OoOoOO00 / O0
   if 84 - 84: oO0o0ooO0
   if 86 - 86: OoOoOO00 - iI1Ii11111iIi - OoO0O00 * ii1II11I1ii1I
   if 66 - 66: OoooooooOO + O0
   if 11 - 11: oO0ooO + OoooooooOO - OoO0O00 / o0oOOo0O0Ooo + Oo0Ooo . II111iiii
   if 41 - 41: iI1Ii11111iIi - O0 - O0
   if 68 - 68: ii11ii1ii % iiIIIII1i1iI
   if 88 - 88: iIii1I11I1II1 - o00ooo0 + ii11ii1ii
   if 40 - 40: I1IiiI * iI1Ii11111iIi + ii11ii1ii % ii1II11I1ii1I
   if 74 - 74: OOooOOo - Oo0Ooo + OoooooooOO + iiIIIII1i1iI / OoOoOO00
   if 23 - 23: O0
   if 85 - 85: iI1Ii11111iIi
OO = "report_"
oo000o = "report_"
iiIi1IIi1I = "report_"
if 84 - 84: o00ooo0 * II111iiii + Oo0Ooo
class O0ooO0Oo00o ( models . Model ) :
 _name = 'cf.cfprint.license'
 _description = '许可证信息'
 if 77 - 77: iIii1I11I1II1 * OoO0O00
 mcode = fields . Char ( string = '机器码' , default = lambda oOooOo0 : I11iii . get_machine_code ( ) , help = '服务器机器码' )
 license = fields . Binary ( string = '许可证' , help = '授权许可证文件，下载后改名为cfprint.lic放到客户端cfprint目录下。' )
 note = fields . Char ( string = '备注' )
 if 38 - 38: iiIIIII1i1iI
 @ api . model
 def create_or_show_license ( self ) :
  Ooo00o0Oooo = I11iii . get_machine_code ( )
  OOooooO0Oo = self . search ( [ ( 'mcode' , '=' , Ooo00o0Oooo ) ] , limit = 1 )
  if not OOooooO0Oo :
   OOooooO0Oo = self . create ( { "mcode" : Ooo00o0Oooo , "note" : "康虎云报表免写代码模块许可证" } )
  OOiIiIIi1 = {
 'type' : 'ir.actions.act_window' ,
 'name' : _ ( '打印服务器地址' ) ,
 'view_mode' : 'form' ,
 'view_type' : 'form' ,
 'res_model' : 'cf.cfprint.license' ,
 'nodestroy' : 'true' ,
 'res_id' : OOooooO0Oo . id ,
 'views' : [ ( False , 'form' ) ] ,

  'target' : 'current' ,
  }
  return OOiIiIIi1
  if 7 - 7: o00ooo0 - Oo0Ooo - OOooOOo + o00ooo0
 @ api . model
 def create ( self , vals ) :
  vals [ 'mcode' ] = iI1I11iiI1i = I11iii . get_machine_code ( ) or ''
  return super ( O0ooO0Oo00o , self ) . create ( vals )
  if 78 - 78: OOooOOo % O0 % iI1Ii11111iIi
  if 46 - 46: OoooooooOO . i11iIiiIii
 def write ( self , vals ) :
  vals [ 'mcode' ] = iI1I11iiI1i = I11iii . get_machine_code ( ) or ''
  return super ( O0ooO0Oo00o , self ) . write ( vals )
  if 94 - 94: o0oOOo0O0Ooo * iI1Ii11111iIi / Oo0Ooo / iI1Ii11111iIi
  if 87 - 87: Oo0Ooo . oO0o0ooO0
 def name_get ( self ) :
  return [ ( O0OO0O . id , "康虎云报表许可证" ) for O0OO0O in self ]
  if 81 - 81: OOooOOo . o0oOOo0O0Ooo % O0 / I1IiiI - OOooOOo
class Ii1I1i ( models . Model ) :
 _inherit = 'ir.model'
 if 99 - 99: OOooOOo . ii1II11I1ii1I + o00ooo0 % OOooOOo . i11iIiiIii % O0
 def name_get ( self ) :
  return [ ( oOO00O . id , '%s(%s)' % ( oOO00O . name , oOO00O . model ) ) for oOO00O in self ]
  if 77 - 77: Oo0Ooo - i1IIi - oO0ooO . OoOoOO00
class IiI1i ( models . Model ) :
 _name = 'cf.report.define.category'
 _description = '报表定义类别'
 if 92 - 92: oO0o0ooO0 . oO0o0ooO0 + OoO0O00
 name = fields . Char ( string = "类别名称" , required = True , help = "为便于管理，报表定义进行分类。默认是“未分类”。" )
 lines = fields . One2many ( "cf.report.define" , "category_id" , string = "报表" )
 note = fields . Text ( string = "备注" )
 if 9 - 9: I1IiiI * O0 + oO0o0ooO0 - oO0ooO * iiIIIII1i1iI
class Oooo0oOO ( models . Model ) :
 _name = 'cf.report.printer'
 _description = '打印机名称'
 if 81 - 81: O0 - o00ooo0 / o0oOOo0O0Ooo % iI1Ii11111iIi
 name = fields . Char ( string = "打印机名称" , required = True , help = "报表打印要使用的客户端打印机名称，不设置则使用默认打印机。\n如果不清楚打印机名称，请不要填写！" )
 note = fields . Text ( string = "备注" )
 if 83 - 83: o00ooo0
class oO00Oo0O0o ( models . Model ) :
 _name = 'cf.report.define'
 _description = '报表定义'
 if 13 - 13: OoooooooOO
 def _compute_technical_name ( self ) :
  for I111iI in self :
   I111iI . technical_name = I111iI . _get_report_name ( )
   if 56 - 56: I1IiiI
 name = fields . Char ( string = '报表ID' , required = True , copy = True , help = "用一确定报表的唯一ID，只允许英文、数字和下划线。" )
 comment = fields . Char ( string = '报表中文名称' , required = True , copy = True )
 technical_name = fields . Char ( string = "技术名称" , readonly = True , compute = "_compute_technical_name" , help = "报表的技术名称，主要用于其他地方直接调用报表。" )
 model_id = fields . Many2one ( 'ir.model' , string = '数据表(model)' , required = True , copy = True , help = "报表对应的数据表(model)" )
 template_id = fields . Many2one ( 'cf.template' , string = '报表模板' , copy = True , help = "该报表使用的打印模板。\n模板如果尚未设计，可以先创建一个模板定义，待生成数据并设计报表模板后再上传到模板库。" )
 company_id = fields . Many2one ( 'res.company' , string = '所属公司' , default = lambda O0oO : O0oO . env [ 'res.company' ] . _company_default_get ( '' ) )
 open_print = fields . Boolean ( string = "是否弹出打印" , default = False )
 hide_print_menu = fields . Boolean ( string = "隐藏打印菜单" , default = False , help = "是否隐藏打印菜单。如果隐藏，则需要通过二次开发来创建菜单或按钮调用报表。" )
 use_client_templ = fields . Boolean ( string = "使用客户端模板" , default = False , help = "打印时使用保存在打印客户端的打印模板。如果是，则需要输入client_templ_name" )
 client_templ_name = fields . Char ( string = "客户端模板文件名" , help = "如果设置了使用客户端模板，则在此录入客户端模板路径和文件名" )
 field_ids = fields . One2many ( "cf.report.define.field" , "report_id" , domain = lambda O0oO : [ ( 'model_id' , '=' , O0oO . model_id . id ) ] , string = "字段" , help = "要在报表模板中使用的字段信息" )
 prn_server_address = fields . Char ( string = "打印服务器地址" , default = "127.0.0.1" , help = "康虎云报表打印服务器地址，默认是127.0.0.1。\n如果不清楚该参数的含义，请勿修改该参数！" )
 prn_server_port = fields . Integer ( string = "打印服务器端口" , default = "54321" , help = "康虎云报表打印服务器端口，默认是54321。\n如果不清楚该参数的含义，请勿修改该参数！" )
 printer_id = fields . Many2one ( "cf.report.printer" , string = "打印机" , help = "要使用的打印机，留空则使用默认打印机" )
 category_id = fields . Many2one ( "cf.report.define.category" , string = "报表分类" , help = "报表类别，默认为未分类" )
 back_after_print = fields . Boolean ( string = "打印后返回" , default = False , help = "打印请求发送到打印伺服器后返回前页" )
 state = fields . Selection ( [ ( 'draft' , '草稿' ) , ( 'defined' , '完成报表定义' ) ] , string = "状态" , default = "draft" )
 note = fields . Text ( string = "备注" )
 if 73 - 73: I1ii11iIi11i * i11iIiiIii % OOooOOo . I1ii11iIi11i
 _sql_constraints = [
 ( 'uniq_name' , 'unique(name)' , _ ( '报表名称必须唯一!' ) ) ,
 ]
 if 66 - 66: OOooOOo + OOooOOo + o00ooo0 / ii1II11I1ii1I + ii11ii1ii
 @ api . model
 def create ( self , vals ) :
  if not vals . get ( "template_id" , False ) :
   iI = vals . get ( "name" , False )
   ii1111iII = vals . get ( "comment" , False )
   if not iI :
    raise ValidationError ( _ ( "请先指定报表ID！" ) )
   iiiiI = "cf_templ_%s" % ( oo000o , iI . replace ( '.' , '_' ) )
   oooOo0OOOoo0 = self . env [ "cf.template" ] . search ( [ ( 'templ_id' , '=' , iiiiI ) ] , limit = 1 )
   if not oooOo0OOOoo0 :
    oooOo0OOOoo0 = self . env [ "cf.template" ] . create ( {
 "templ_id" : iiiiI ,
 "name" : ( ii1111iII or iiiiI ) + "打印模板" ,
 "description" : ( ii1111iII or iiiiI ) + "打印模板" ,
 } )
   vals [ "template_id" ] = oooOo0OOOoo0 . id
   if 51 - 51: Oo0Ooo / OoOoOO00 . ii11ii1ii * o0oOOo0O0Ooo + OoO0O00 * oO0o0ooO0
  return super ( oO00Oo0O0o , self ) . create ( vals )
  if 73 - 73: OoO0O00 + OoooooooOO - O0 - iI1Ii11111iIi - II111iiii
  if 99 - 99: o00ooo0 . iI1Ii11111iIi + iiIIIII1i1iI + OoooooooOO % o0oOOo0O0Ooo
 def unlink ( self ) :
  for ooO in self :
   ooO . _remove_report ( )
  return super ( oO00Oo0O0o , self ) . unlink ( )
  if 46 - 46: I1IiiI - OoooooooOO - oO0ooO * II111iiii
 def _get_report_id ( self ) :
  self . ensure_one ( )
  return "%s%s" % ( iiIi1IIi1I , self . name )
  if 34 - 34: oO0ooO - ii1II11I1ii1I / ii11ii1ii + I1ii11iIi11i * iI1Ii11111iIi
 def _get_report_name ( self , with_module = True ) :
  self . ensure_one ( )
  if with_module :
   return "cf_report_designer.%s%s" % ( oo000o , self . name . replace ( '.' , '_' ) )
  else :
   return "%s%s" % ( oo000o , self . name . replace ( '.' , '_' ) )
   if 73 - 73: OoOoOO00 . iI1Ii11111iIi * I1ii11iIi11i % I1ii11iIi11i % OoooooooOO
 def _get_report_file ( self , with_module = True ) :
  self . ensure_one ( )
  if with_module :
   return "cf_report_designer.%s%s" % ( OO , self . name . replace ( '.' , '_' ) )
  else :
   return "%s%s" % ( OO , self . name . replace ( '.' , '_' ) )
   if 63 - 63: iIii1I11I1II1 * i11iIiiIii % iIii1I11I1II1 * i11iIiiIii
   if 32 - 32: ii11ii1ii
 def _remove_report ( self ) :
  I11iiiiIIii1I = self . _get_report_id ( )
  II1IiiIi1i = self . _get_report_name ( )
  iiI11ii1I1 = self . _get_report_file ( )
  if 82 - 82: II111iiii % oO0ooO / OoO0O00 + OoOoOO00 / o0oOOo0O0Ooo / iiIIIII1i1iI
  if 70 - 70: OOooOOo
  self . env [ "ir.model.data" ] . sudo ( ) . search ( [ ( 'name' , '=' , I11iiiiIIii1I ) ] ) . unlink ( )
  if 59 - 59: o0oOOo0O0Ooo % OOooOOo
  ii1iI1I11I = self . env [ 'ir.actions.report' ] . sudo ( ) . search ( [ ( 'report_name' , '=' , II1IiiIi1i ) ] )
  for ooO in ii1iI1I11I :
   ooO . unlink_action ( )
   ooO . unlink ( )
   if 20 - 20: OOooOOo / O0 * o0oOOo0O0Ooo - iiIIIII1i1iI % OoooooooOO * oO0o0ooO0
   if 18 - 18: Oo0Ooo * iiIIIII1i1iI + iiIIIII1i1iI * i11iIiiIii * iIii1I11I1II1 - o00ooo0
  self . env [ 'ir.ui.view' ] . search ( [ ( 'key' , '=' , II1IiiIi1i ) ] ) . unlink ( )
  if 29 - 29: OoOoOO00 - oO0o0ooO0 * OoooooooOO + OoooooooOO . II111iiii + OoooooooOO
  if 74 - 74: iI1Ii11111iIi - oO0o0ooO0 / ii1II11I1ii1I * O0 - ii11ii1ii
  if 19 - 19: I1IiiI
  if 25 - 25: iI1Ii11111iIi / o00ooo0
  if 31 - 31: ii11ii1ii . O0 % I1IiiI . o0oOOo0O0Ooo + oO0o0ooO0
  if 71 - 71: iiIIIII1i1iI . II111iiii
  if 62 - 62: OoooooooOO . oO0ooO
  if 61 - 61: OoOoOO00 - ii11ii1ii - i1IIi
  if 25 - 25: O0 * oO0ooO + I1ii11iIi11i . o0oOOo0O0Ooo . o0oOOo0O0Ooo
 def action_retrieve_fields ( self ) :
  if 58 - 58: I1IiiI
  self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . id ) ] ) . unlink ( )
  if 53 - 53: i1IIi
  if 59 - 59: o0oOOo0O0Ooo
  if 81 - 81: OoOoOO00 - OoOoOO00 . ii1II11I1ii1I
  for o0OoOo00o0o in self . model_id . field_id :
   if 41 - 41: o00ooo0 % OoO0O00 - Oo0Ooo * iiIIIII1i1iI * Oo0Ooo
   OOOoOO0o = self . env [ 'cf.report.define.field' ] . create ( {
 "report_id" : self . id ,
 "model_id" : o0OoOo00o0o . model_id . id ,
 "field_id" : o0OoOo00o0o . id ,

   } )
   if 1 - 1: II111iiii
 def action_remove_fields ( self ) :
  self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . id ) ] ) . unlink ( )
  if 68 - 68: ii1II11I1ii1I - I1IiiI / iiIIIII1i1iI / oO0ooO
  if 12 - 12: iI1Ii11111iIi + i11iIiiIii * iIii1I11I1II1 / I1ii11iIi11i . oO0ooO
 def _make_report_defind ( self ) :
  I11iiiiIIii1I = self . _get_report_id ( )
  if 5 - 5: i1IIi + oO0o0ooO0 / o0oOOo0O0Ooo . ii1II11I1ii1I / oO0ooO
  II1IiiIi1i = self . _get_report_name ( )
  iiI11ii1I1 = self . _get_report_file ( )
  if 32 - 32: I1IiiI % iIii1I11I1II1 / i1IIi - I1IiiI
  if 7 - 7: iiIIIII1i1iI * OoO0O00 - o00ooo0 + ii11ii1ii * I1IiiI % OoO0O00
  iI1i111I1Ii = self . env [ 'ir.actions.report' ]
  i11i1ii1I = iI1i111I1Ii . create ( {
 "name" : self . comment or self . name ,
 "type" : "ir.actions.report" ,
 "binding_type" : "report" ,
 "model" : self . model_id . model ,
 "report_type" : "qweb-html" ,
 "report_name" : II1IiiIi1i ,
 "report_file" : iiI11ii1I1 ,
  "multi" : False ,
 "print_report_name" : self . comment or self . name ,
  "attachment_use" : False ,
 "cf_report_define_id" : self . id ,

  # iI1Ii11111iIi / I1ii11iIi11i % oO0o0ooO0 + o00ooo0 / iiIIIII1i1iI . o00ooo0
  } )
  if i11i1ii1I :
   self . env [ "ir.model.data" ] . create ( {
 "name" : "action_%s" % ( I11iiiiIIii1I ) ,
 "model" : "ir.actions.report" ,
 "module" : "cf_report_designer" ,
 "noupdate" : False ,
 "res_id" : i11i1ii1I . id
 } )
   if 12 - 12: i1IIi + i1IIi - I1ii11iIi11i * Oo0Ooo % Oo0Ooo - II111iiii
   i11i1ii1I . create_action ( )
   if 52 - 52: o00ooo0 . ii1II11I1ii1I + iiIIIII1i1iI
 def _make_templ ( self ) :
  if 38 - 38: i1IIi - II111iiii . iiIIIII1i1iI
  if 58 - 58: I1IiiI . ii1II11I1ii1I + OoOoOO00
  O00OO = "%s%s" % ( oo000o , self . name . replace ( '.' , '_' ) )
  I11iiiiIIii1I = self . _get_report_id ( )
  II1IiiIi1i = self . _get_report_name ( )
  iiI11ii1I1 = self . _get_report_file ( )
  if 17 - 17: oO0ooO / iiIIIII1i1iI + OOooOOo - i11iIiiIii . ii1II11I1ii1I
  OO0o0oOOO0O = self . _get_report_name ( False )
  if 49 - 49: I1ii11iIi11i . o0oOOo0O0Ooo . II111iiii
  o000ooooO0o = """<?xml version="1.0"?>
<t t-name="%s">
  <t t-call="cfprint.html_container">
    <t t-raw="show_message"/>
  </t>
<script type="text/javascript">
  <t t-raw="cfprint_json"/>
</script>
</t>
""" % ( OO0o0oOOO0O )
  if 40 - 40: I1ii11iIi11i + i1IIi * ii11ii1ii
  O0oOOoooOO0O = self . env [ 'ir.ui.view' ]
  if 86 - 86: o0oOOo0O0Ooo
  try :
   i1Iii11Ii1i1 = O0oOOoooOO0O . create ( {
 "name" : I11iiiiIIii1I ,
 "key" : II1IiiIi1i ,
 "priority" : 16 ,
 "type" : "qweb" ,
 "arch_db" : o000ooooO0o ,
 "mode" : "primary" ,
 "active" : True ,

   } )
   if i1Iii11Ii1i1 :
    if 59 - 59: Oo0Ooo % OoooooooOO . ii1II11I1ii1I / oO0o0ooO0 + I1IiiI
    self . env [ "ir.model.data" ] . create ( {
 "name" : OO0o0oOOO0O ,
 "model" : "ir.ui.view" ,
 "module" : "cf_report_designer" ,
 "noupdate" : False ,
 "res_id" : i1Iii11Ii1i1 . id
 } )
    if 76 - 76: o00ooo0
  except Exception as I1IiI :
   O00ooOO . error ( "Create report template[%s] failed." % ( II1IiiIi1i ) )
   raise I1IiI
   if 73 - 73: O0 * ii1II11I1ii1I + iI1Ii11111iIi + o00ooo0
 def action_generate ( self ) :
  if 40 - 40: II111iiii . OoOoOO00 * iiIIIII1i1iI + ii11ii1ii + ii11ii1ii
  if 9 - 9: oO0ooO % OoooooooOO . OOooOOo % oO0ooO
  if 32 - 32: i11iIiiIii
  self . _remove_report ( )
  if 31 - 31: iIii1I11I1II1 / OoO0O00 / I1ii11iIi11i
  if 41 - 41: Oo0Ooo
  self . _make_report_defind ( )
  if 10 - 10: Oo0Ooo / Oo0Ooo / iiIIIII1i1iI . iiIIIII1i1iI
  if 98 - 98: Oo0Ooo / I1IiiI . O0 + OoO0O00
  self . _make_templ ( )
  if 43 - 43: II111iiii . OOooOOo / I1ii11iIi11i
  self . write ( { "state" : "defined" } )
  if 20 - 20: I1IiiI
 def action_design ( self ) :
  if 95 - 95: ii1II11I1ii1I - I1IiiI
  if 34 - 34: o00ooo0 * I1IiiI . i1IIi * o00ooo0 / o00ooo0
  if 30 - 30: I1ii11iIi11i + Oo0Ooo / Oo0Ooo % I1ii11iIi11i . I1ii11iIi11i
  O0O0Oo00 = self . env [ self . model_id . model ] . search ( [ ] , limit = 5 )
  oOoO00o = [ oOooOo0 . id for oOooOo0 in O0O0Oo00 ]
  if 100 - 100: o0oOOo0O0Ooo + ii11ii1ii * o0oOOo0O0Ooo
  if 80 - 80: o0oOOo0O0Ooo * O0 - iI1Ii11111iIi
  I11iiiiIIii1I = "cf_report_designer.%s%s" % ( iiIi1IIi1I , self . name )
  if 66 - 66: i11iIiiIii - ii11ii1ii * Oo0Ooo
  II1IiiIi1i = "cf_report_designer.%s%s" % ( oo000o , self . name )
  OooOOOO = { "is_design" : True ,
 "docs" : O0O0Oo00 ,
 "docids" : oOoO00o
 }
  if 45 - 45: I1ii11iIi11i % I1IiiI - i11iIiiIii
  return ( self . env [ 'ir.actions.report' ] . search ( [ ( 'report_name' , '=' , II1IiiIi1i ) ] , limit = 1 )
 . with_context ( { 'is_design' : True } )
 . report_action ( oOoO00o , data = OooOOOO ) )
  if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * I1IiiI
  if 46 - 46: OoOoOO00 + OoO0O00
class o0o0O ( models . Model ) :
 _name = 'cf.report.define.field'
 _description = '报表字段'
 _order = 'report_id, id'
 if 68 - 68: o00ooo0
 report_id = fields . Many2one ( "cf.report.define" , string = "报表定义" , required = True , ondelete = 'cascade' , help = "字段所在的报表定义" )
 model_id = fields . Many2one ( 'ir.model' , string = "数据表(模型)" , required = True , ondelete = 'cascade' , help = "字段所在的model" )
 model_name = fields . Char ( related = "model_id.name" , string = "模型名称" )
 field_id = fields . Many2one ( "ir.model.fields" , string = "字段" , required = True , ondelete = 'cascade' )
 name = fields . Char ( related = "field_id.name" , string = '字段名称' )
 field_description = fields . Char ( related = "field_id.field_description" , string = '字段说明' )
 ttype = fields . Selection ( related = "field_id.ttype" , string = '字段类型' )
 related_field_id = fields . Many2one ( "cf.report.define.field" , string = "关联字段" , help = "与关联表关联的字段(related_external_field_ids)" )
 related_external_field_ids = fields . One2many ( "cf.report.define.field" , "related_field_id" , string = "关联数据表字段" , help = "与当前表相关联的表字段" )
 note = fields . Text ( string = "备注" )
 if 25 - 25: I1ii11iIi11i . o00ooo0
 related_field_model_id = fields . Many2one ( 'ir.model' , compute = "_compute_relation_model" , string = "关联数据表（模型）" , help = "关联字段所在的model。当前字段为One2many，Many2many，Many2one时有值。" )
 if 24 - 24: OOooOOo / i11iIiiIii + OOooOOo
 related_field_model_name = fields . Char ( compute = "_compute_relation_model" , string = "关联数据表名称" , help = "关联字段所在的model名称" )
 if 20 - 20: oO0ooO + iI1Ii11111iIi / O0 % iIii1I11I1II1
 _sql_constraints = [
 ( 'uniq_repoer_model_field' , 'unique(report_id, model_id, related_field_id, field_id)' , '报表 + 表 + 关联上级字段 + 字段必须唯一!' ) ,
 ]
 if 88 - 88: OoOoOO00 / II111iiii
 @ api . model
 def create ( self , vals ) :
  if 87 - 87: I1ii11iIi11i - I1ii11iIi11i - ii1II11I1ii1I + OOooOOo
  if not vals . get ( "model_id" , False ) :
   OOOoOO0o = self . env [ "ir.model.fields" ] . browse ( vals . get ( "field_id" , 0 ) )
   if OOOoOO0o :
    vals [ "model_id" ] = OOOoOO0o . model_id . id
    if 82 - 82: OOooOOo / iIii1I11I1II1 . I1IiiI . ii11ii1ii / o0oOOo0O0Ooo
    if 42 - 42: Oo0Ooo
  self . search ( [ ( 'report_id' , '=' , vals . get ( "report_id" , 0 ) ) , ( 'model_id' , '=' , vals . get ( "model_id" , 0 ) ) ,
 ( 'related_field_id' , '=' , vals . get ( "related_field_id" , 0 ) ) , ( 'field_id' , '=' , vals . get ( "field_id" , 0 ) ) ] ) . unlink ( )
  if 19 - 19: OOooOOo % I1ii11iIi11i * iIii1I11I1II1 + I1IiiI
  return super ( o0o0O , self ) . create ( vals )
  if 46 - 46: Oo0Ooo
 def _compute_relation_model ( self ) :
  for OOOoOO0o in self :
   i1II1I1Iii1 = self . env [ 'ir.model' ] . _get ( OOOoOO0o . field_id . relation )
   OOOoOO0o . related_field_model_id = i1II1I1Iii1 . id if i1II1I1Iii1 else None
   OOOoOO0o . related_field_model_name = i1II1I1Iii1 . name if i1II1I1Iii1 else None
   if 30 - 30: OoooooooOO - OoOoOO00
 def action_retrieve_fields ( self ) :
  if self . field_id and ( self . field_id . ttype == 'one2many' or self . field_id . ttype == 'many2many' or self . field_id . ttype == 'many2one' ) :
   if 75 - 75: iIii1I11I1II1 - iI1Ii11111iIi . Oo0Ooo % i11iIiiIii % oO0ooO
   if self . env . get ( self . field_id . relation , '_EMPTY' ) == '_EMPTY' :
    raise AccessError ( _ ( "未找到关联字段对应的表（%s），无法获取关联表字段！" % ( self . field_id . relation ) ) )
    if 55 - 55: ii1II11I1ii1I . II111iiii % OoO0O00 * ii1II11I1ii1I + o00ooo0 + iI1Ii11111iIi
    if 24 - 24: Oo0Ooo - OOooOOo % iIii1I11I1II1 . i1IIi / O0
   ii1ii111 = self . env [ 'ir.model' ] . _get ( self . field_id . relation )
   if 10 - 10: iiIIIII1i1iI % oO0o0ooO0 * oO0o0ooO0 . oO0ooO / iI1Ii11111iIi % ii11ii1ii
   if 49 - 49: OoO0O00 / OOooOOo + O0 * o0oOOo0O0Ooo
   self . action_remove_fields ( )
   if 28 - 28: o00ooo0 + i11iIiiIii / oO0ooO % OoOoOO00 % Oo0Ooo - O0
   if 54 - 54: i1IIi + II111iiii
   for o0OoOo00o0o in ii1ii111 . field_id :
    OOOoOO0o = self . env [ 'cf.report.define.field' ] . create ( {
 "related_field_id" : self . id ,
 "report_id" : self . report_id . id ,
 "model_id" : o0OoOo00o0o . model_id . id ,
 "field_id" : o0OoOo00o0o . id ,
 } )
    if 83 - 83: I1ii11iIi11i - I1IiiI + ii11ii1ii
 def action_remove_fields ( self ) :
  if self . field_id and ( self . field_id . ttype == 'one2many' or self . field_id . ttype == 'many2many' or self . field_id . ttype == 'many2one' ) :
   if 5 - 5: iI1Ii11111iIi
   ii1ii111 = self . env [ 'ir.model' ] . _get ( self . field_id . relation )
   if 46 - 46: oO0o0ooO0
   if 45 - 45: o00ooo0
   self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . report_id . id ) , ( 'model_id' , '=' , ii1ii111 . id ) , ( 'related_field_id' , '=' , self . id ) ] ) . unlink ( )
   if 21 - 21: OOooOOo . iiIIIII1i1iI . ii11ii1ii / Oo0Ooo / iiIIIII1i1iI
 def action_view_sub_fields ( self ) :
  self . ensure_one ( )
  if 17 - 17: ii11ii1ii / ii11ii1ii / oO0ooO
  ii1 = self . env . ref ( 'cf_report_designer.cf_report_define_field_form' ) . id
  return { 'type' : 'ir.actions.act_window' ,
 'res_model' : 'cf.report.define.field' ,
 'view_mode' : 'form' ,
 'views' : [ ( ii1 , 'form' ) ] ,
 'res_id' : self . id ,
 'target' : 'new' ,
 'limit' : 1000 ,
 'name' : '关联表字段' ,
 'flags' : { 'form' : { 'action_buttons' : False } }
 }
  if 1 - 1: o00ooo0 % iIii1I11I1II1 + Oo0Ooo . iIii1I11I1II1 % I1IiiI
  if 89 - 89: iI1Ii11111iIi
  if 76 - 76: o00ooo0
  if 15 - 15: ii11ii1ii . oO0ooO + OoooooooOO - OoO0O00
  if 69 - 69: iIii1I11I1II1 . I1ii11iIi11i % o00ooo0 + iIii1I11I1II1 / O0 / I1ii11iIi11i
  if 61 - 61: ii11ii1ii % ii11ii1ii * o0oOOo0O0Ooo / o0oOOo0O0Ooo
  if 75 - 75: oO0o0ooO0 . o00ooo0
from xml . dom import minidom
import uuid
if 50 - 50: OoOoOO00
O00o0OO0000oo = "<h5 style=\"margin-top: 3rem; text-align: center;\">%s</h4>"
if 27 - 27: O0
if 79 - 79: o0oOOo0O0Ooo - oO0ooO + o0oOOo0O0Ooo . OOooOOo
class ii1III11 ( models . Model ) :
 if 7 - 7: ii1II11I1ii1I % O0 . OoOoOO00 + I1IiiI - oO0ooO
 _inherit = 'ir.actions.report'
 if 75 - 75: oO0ooO
 if 71 - 71: o00ooo0
 if 53 - 53: OoooooooOO % iI1Ii11111iIi . oO0o0ooO0 / i11iIiiIii % ii1II11I1ii1I
 _description = 'Report Action'
 if 28 - 28: oO0ooO
 cf_report_define_id = fields . Many2one ( "cf.report.define" , string = "报表定义" , help = "如果是康虎云报表，则保存对应的报表定义。" )
 if 58 - 58: OoOoOO00
 def _make_cfprint_json ( self , values ) :
  if 37 - 37: Oo0Ooo - iIii1I11I1II1 / I1ii11iIi11i
  if 73 - 73: i11iIiiIii - oO0o0ooO0
  def ii11I1 ( lst ) :
   oO0oo = set ( )
   if 38 - 38: OoooooooOO * o00ooo0 % O0 * OoOoOO00
   if 29 - 29: I1ii11iIi11i / i1IIi . I1IiiI - OoOoOO00 - OoOoOO00 - iI1Ii11111iIi
   if 20 - 20: i1IIi % OoO0O00 . I1IiiI / oO0o0ooO0 * i11iIiiIii * ii11ii1ii
   if 85 - 85: o0oOOo0O0Ooo . OoOoOO00 / o00ooo0 . O0 % iiIIIII1i1iI
   if 90 - 90: Oo0Ooo % O0 * iIii1I11I1II1 . ii1II11I1ii1I
   I1iii11 = [ ]
   ooo0O = time . clock ( )
   for iII1iii in lst :
    i11i1iiiII = tuple ( iII1iii . items ( ) )
    if i11i1iiiII not in oO0oo :
     oO0oo . add ( i11i1iiiII )
     I1iii11 . append ( iII1iii )
     if 68 - 68: i11iIiiIii * OoO0O00
   II1i = time . clock ( )
   print ( "_remove_duplicated consume: %f" % ( ( II1i - ooo0O ) ) )
   return I1iii11
   if 2 - 2: iIii1I11I1II1 * Oo0Ooo % OOooOOo - II111iiii - ii1II11I1ii1I
  def iIi11iiIiI1I ( field ) :
   IiiioooOOoooo = "str"
   if 89 - 89: ii1II11I1ii1I - o00ooo0 % Oo0Ooo % o0oOOo0O0Ooo
   if 49 - 49: Oo0Ooo - I1IiiI / oO0o0ooO0 / O0 % o0oOOo0O0Ooo * iI1Ii11111iIi
   if 100 - 100: ii11ii1ii . ii1II11I1ii1I / O0 * i1IIi * iI1Ii11111iIi * Oo0Ooo
   if 84 - 84: I1ii11iIi11i / ii11ii1ii % i11iIiiIii * iiIIIII1i1iI % I1ii11iIi11i - OoooooooOO
   if 99 - 99: I1IiiI + O0 + i1IIi / i11iIiiIii - i1IIi * iIii1I11I1II1
   if field . ttype in [ "binary" ] :
    IiiioooOOoooo = "blob"
   elif field . ttype in [ "boolean" ] :
    IiiioooOOoooo = "boolean"
   elif field . ttype in [ 'char' , 'selection' , 'reference' ] :
    IiiioooOOoooo = "str"
   elif field . ttype in [ 'text' , 'html' ] :
    IiiioooOOoooo = "text"
   elif field . ttype in [ 'date' , 'datetime' ] :
    IiiioooOOoooo = "date"
   elif field . ttype in [ 'float' , 'monetary' ] :
    IiiioooOOoooo = "float"
   elif field . ttype in [ "integer" , "many2one" ] :
    IiiioooOOoooo = "int"
   return IiiioooOOoooo
   if 72 - 72: I1IiiI * I1ii11iIi11i . iI1Ii11111iIi * oO0o0ooO0 * Oo0Ooo * iiIIIII1i1iI
  def iii11 ( report_define , model , fields , docs , datas , related_field = False ) :
   O000 = { }
   if 79 - 79: OoooooooOO - I1IiiI
   if 69 - 69: oO0ooO
   if 95 - 95: o00ooo0 + i11iIiiIii * iiIIIII1i1iI - i1IIi * iiIIIII1i1iI - iIii1I11I1II1
   if 75 - 75: OoooooooOO * oO0o0ooO0
   if 9 - 9: oO0o0ooO0 - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
   if 39 - 39: oO0o0ooO0 * Oo0Ooo + iIii1I11I1II1 - oO0o0ooO0 + ii11ii1ii
   if 69 - 69: O0
   if 85 - 85: o00ooo0 / O0
   if 18 - 18: o0oOOo0O0Ooo % O0 * I1ii11iIi11i
   if 62 - 62: iiIIIII1i1iI . oO0o0ooO0 . OoooooooOO
   if 11 - 11: ii11ii1ii / oO0ooO
   oooO0 = model . model . replace ( "." , "_" )
   if 16 - 16: II111iiii + OOooOOo - OoooooooOO
   if 3 - 3: O0 / ii1II11I1ii1I
   if 31 - 31: ii11ii1ii + o0oOOo0O0Ooo . OoooooooOO
   if 89 - 89: II111iiii + i1IIi + II111iiii
   if 7 - 7: O0 % o0oOOo0O0Ooo + I1ii11iIi11i * ii1II11I1ii1I - ii1II11I1ii1I
   if 42 - 42: OoOoOO00 * OoOoOO00 * iiIIIII1i1iI . oO0ooO
   if not datas . get ( oooO0 , False ) :
    datas [ oooO0 ] = { "cols" : [ ] , "rows" : [ ] }
    if 51 - 51: ii11ii1ii % iIii1I11I1II1 - OoooooooOO % o00ooo0 * iIii1I11I1II1 % OoO0O00
   oO0o00oOOooO0 = datas [ oooO0 ] [ "cols" ]
   if 79 - 79: OoO0O00 - iIii1I11I1II1 + iI1Ii11111iIi - iiIIIII1i1iI
   OoO = 255
   if 35 - 35: OoOoOO00 + i11iIiiIii - II111iiii
   ooo0O = time . clock ( )
   for O0OO0O in docs :
    Ii1ii111i1 = { }
    for OOOoOO0o in [ iII1iii for iII1iii in fields if iII1iii . model_id . model == model . model ] :
     try :
      if OOOoOO0o . ttype == 'binary' :
       Ii1ii111i1 [ OOOoOO0o . name ] = "base64/jpg:%s" % ( O0OO0O [ OOOoOO0o . name ] . strip ( ) . decode ( "UTF-8" ) . replace ( "\n" , "" ) if O0OO0O [ OOOoOO0o . name ] else "" )
       if 31 - 31: ii11ii1ii + O0
      elif OOOoOO0o . ttype in [ 'boolean' ] :
       Ii1ii111i1 [ OOOoOO0o . name ] = O0OO0O [ OOOoOO0o . name ]
       if 87 - 87: o00ooo0
      elif OOOoOO0o . ttype in [ 'char' , 'text' , 'html' , 'reference' ] :
       Ii1ii111i1 [ OOOoOO0o . name ] = O0OO0O [ OOOoOO0o . name ] if O0OO0O [ OOOoOO0o . name ] else ""
       if len ( Ii1ii111i1 [ OOOoOO0o . name ] ) > O000 . get ( OOOoOO0o . name , OoO ) :
        O000 [ OOOoOO0o . name ] = len ( Ii1ii111i1 [ OOOoOO0o . name ] )
        if 45 - 45: OoO0O00 / OoooooooOO - ii1II11I1ii1I / iI1Ii11111iIi % oO0o0ooO0
      elif OOOoOO0o . ttype in [ 'date' , 'datetime' ] :
       Ii1ii111i1 [ OOOoOO0o . name ] = O0OO0O [ OOOoOO0o . name ] . strftime ( "%Y-%m-%d %H:%M:%S" ) if O0OO0O [ OOOoOO0o . name ] else ""
       if 83 - 83: I1IiiI . iIii1I11I1II1 - oO0o0ooO0 * i11iIiiIii
      elif OOOoOO0o . ttype in [ 'float' , 'integer' , 'monetary' ] :
       Ii1ii111i1 [ OOOoOO0o . name ] = O0OO0O [ OOOoOO0o . name ] if O0OO0O [ OOOoOO0o . name ] != None else ""
       if 20 - 20: i1IIi * iiIIIII1i1iI + II111iiii % o0oOOo0O0Ooo % OOooOOo
      elif OOOoOO0o . ttype in [ "one2many" ] and len ( OOOoOO0o . related_external_field_ids ) > 0 :
       if 13 - 13: Oo0Ooo
       oOOo000oOoO0 = O0OO0O [ OOOoOO0o . name ]
       OoOo00o0OO = OOOoOO0o . related_external_field_ids
       ii1IIIIiI11 = self . env [ 'ir.model' ] . _get ( OOOoOO0o . field_id . relation )
       if 40 - 40: o0oOOo0O0Ooo
       if OoOo00o0OO and len ( OoOo00o0OO ) > 0 and ii1IIIIiI11 :
        iii11 ( report_define , ii1IIIIiI11 , OoOo00o0OO , oOOo000oOoO0 , datas )
        if 67 - 67: OOooOOo + II111iiii - O0 . OOooOOo * II111iiii * oO0ooO
      elif OOOoOO0o . ttype in [ "many2many" ] and len ( OOOoOO0o . related_external_field_ids ) > 0 :
       Ii1ii111i1 [ OOOoOO0o . name ] = "," . join ( [ str ( oOooOo0 . id ) for oOooOo0 in O0OO0O [ OOOoOO0o . name ] ] )
       oOOo000oOoO0 = O0OO0O [ OOOoOO0o . name ]
       OoOo00o0OO = OOOoOO0o . related_external_field_ids
       ii1IIIIiI11 = self . env [ 'ir.model' ] . _get ( OOOoOO0o . field_id . relation )
       if 90 - 90: iI1Ii11111iIi . oO0o0ooO0
       if OoOo00o0OO and len ( OoOo00o0OO ) > 0 and ii1IIIIiI11 :
        iii11 ( report_define , ii1IIIIiI11 , OoOo00o0OO , oOOo000oOoO0 , datas )
        if 81 - 81: ii11ii1ii - oO0ooO % o00ooo0 - OoO0O00 / Oo0Ooo
      elif OOOoOO0o . ttype in [ 'many2one' ] :
       Ii1ii111i1 [ OOOoOO0o . name ] = O0OO0O [ OOOoOO0o . name ] . id if O0OO0O [ OOOoOO0o . name ] else ""
       Ii1ii111i1 [ OOOoOO0o . name + "_name" ] = O0OO0O [ OOOoOO0o . name ] . name if O0OO0O [ OOOoOO0o . name ] and O0OO0O [ OOOoOO0o . name ] . name else ""
       Ii1ii111i1 [ OOOoOO0o . name + "_display_name" ] = O0OO0O [ OOOoOO0o . name ] . display_name if O0OO0O [ OOOoOO0o . name ] and O0OO0O [ OOOoOO0o . name ] . display_name else ""
       if len ( Ii1ii111i1 [ OOOoOO0o . name + "_name" ] ) > O000 . get ( OOOoOO0o . name + "_name" , OoO ) :
        O000 [ OOOoOO0o . name + "_name" ] = len ( Ii1ii111i1 [ OOOoOO0o . name + "_name" ] )
       if len ( Ii1ii111i1 [ OOOoOO0o . name + "_display_name" ] ) > O000 . get ( OOOoOO0o . name + "_display_name" , OoO ) :
        O000 [ OOOoOO0o . name + "_display_name" ] = len ( Ii1ii111i1 [ OOOoOO0o . name + "_display_name" ] )
        if 4 - 4: OoooooooOO - i1IIi % iI1Ii11111iIi - ii11ii1ii * o0oOOo0O0Ooo
        if 85 - 85: OoooooooOO * iIii1I11I1II1 . ii1II11I1ii1I / OoooooooOO % I1IiiI % O0
       if len ( OOOoOO0o . related_external_field_ids ) > 0 :
        oOOo000oOoO0 = O0OO0O [ OOOoOO0o . name ]
        OoOo00o0OO = OOOoOO0o . related_external_field_ids
        ii1IIIIiI11 = self . env [ 'ir.model' ] . _get ( OOOoOO0o . field_id . relation )
        if 36 - 36: iI1Ii11111iIi / II111iiii / oO0o0ooO0 / oO0o0ooO0 + I1ii11iIi11i
        if OoOo00o0OO and len ( OoOo00o0OO ) > 0 and ii1IIIIiI11 :
         iii11 ( report_define , ii1IIIIiI11 , OoOo00o0OO , oOOo000oOoO0 , datas , OOOoOO0o )
         if 95 - 95: oO0o0ooO0
      elif OOOoOO0o . ttype in [ 'selection' ] :
       Ii1ii111i1 [ OOOoOO0o . name ] = O0OO0O [ OOOoOO0o . name ] if O0OO0O [ OOOoOO0o . name ] else ""
       iI = dict ( O0OO0O . _fields [ OOOoOO0o . name ] . _description_selection ( O0OO0O . env ) ) . get ( Ii1ii111i1 [ OOOoOO0o . name ] , '' )
       Ii1ii111i1 [ OOOoOO0o . name + "_name" ] = iI or ""
       if len ( Ii1ii111i1 [ OOOoOO0o . name + "_name" ] ) > O000 . get ( OOOoOO0o . name + "_name" , OoO ) :
        O000 [ OOOoOO0o . name + "_name" ] = len ( Ii1ii111i1 [ OOOoOO0o . name + "_name" ] )
        if 51 - 51: II111iiii + oO0o0ooO0 . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
     except Exception as OOoOoo0 :
      O00ooOO . error ( _ ( "生成康虎云报表打印数据出错。model: %s, field: %s, Error: %s" ) % ( model . model , OOOoOO0o . name , OOoOoo0 ) )
      pass
      if 17 - 17: iI1Ii11111iIi + OOooOOo . OoO0O00 - Oo0Ooo * i11iIiiIii
    if Ii1ii111i1 :
     if 20 - 20: I1IiiI . OoooooooOO % ii11ii1ii
     if Ii1ii111i1 . get ( "id" ) not in [ oOooOo0 . get ( "id" ) for oOooOo0 in datas [ oooO0 ] [ "rows" ] ] :
      datas [ oooO0 ] [ "rows" ] . append ( Ii1ii111i1 )
      if 63 - 63: I1IiiI % iIii1I11I1II1
      if 39 - 39: ii1II11I1ii1I / II111iiii / I1ii11iIi11i % I1IiiI
   for OOOoOO0o in [ iII1iii for iII1iii in fields if iII1iii . model_id . model == model . model ] :
    IiiioooOOoooo = iIi11iiIiI1I ( OOOoOO0o )
    if 89 - 89: iiIIIII1i1iI + OoooooooOO + iiIIIII1i1iI * i1IIi + iIii1I11I1II1 % oO0ooO
    oOo0oO = OoO
    if IiiioooOOoooo == "str" :
     oOo0oO = O000 . get ( OOOoOO0o . name , OoO )
    if IiiioooOOoooo == "text" :
     oOo0oO = O000 . get ( OOOoOO0o . name , OoO )
     IiiioooOOoooo == "str"
     if 5 - 5: ii11ii1ii - ii11ii1ii . Oo0Ooo + OoOoOO00 - ii11ii1ii . OOooOOo
    datas [ oooO0 ] [ "cols" ] . append ( { "type" : IiiioooOOoooo , "size" : oOo0oO , "name" : OOOoOO0o . name , "required" : False , "comment" : OOOoOO0o . field_description } )
    if 31 - 31: II111iiii - iIii1I11I1II1 - iIii1I11I1II1 % oO0ooO
    if 12 - 12: iIii1I11I1II1
    if 20 - 20: o0oOOo0O0Ooo / i1IIi
    if OOOoOO0o . ttype in [ "one2many" , "many2many" ] :
     datas [ oooO0 ] [ "cols" ] . append ( { "type" : "str" , "size" : O000 . get ( OOOoOO0o . name , OoO ) , "name" : OOOoOO0o . name + "_ids" , "required" : False , "comment" : OOOoOO0o . field_description } )
     if 71 - 71: OoOoOO00 . i1IIi
    if OOOoOO0o . ttype in [ "many2one" ] :
     datas [ oooO0 ] [ "cols" ] . append ( { "type" : "str" , "size" : O000 . get ( OOOoOO0o . name + "_name" , OoO ) , "name" : OOOoOO0o . name + "_name" , "required" : False , "comment" : OOOoOO0o . field_description } )
     datas [ oooO0 ] [ "cols" ] . append ( { "type" : "str" , "size" : O000 . get ( OOOoOO0o . name + "_display_name" , OoO ) , "name" : OOOoOO0o . name + "_display_name" , "required" : False , "comment" : OOOoOO0o . field_description } )
     if 94 - 94: ii11ii1ii . iiIIIII1i1iI
    if OOOoOO0o . ttype in [ "selection" ] :
     datas [ oooO0 ] [ "cols" ] . append ( { "type" : "str" , "size" : O000 . get ( OOOoOO0o . name + "_name" , OoO ) , "name" : OOOoOO0o . name + "_name" , "required" : False , "comment" : OOOoOO0o . field_description } )
     if 84 - 84: O0 . oO0ooO - II111iiii . o00ooo0 / II111iiii
   datas [ oooO0 ] [ "cols" ] = ii11I1 ( datas [ oooO0 ] [ "cols" ] )
   if 47 - 47: OoooooooOO
   II1i = time . clock ( )
   print ( "_make_data_obj[%s] consume: %f" % ( oooO0 , ( II1i - ooo0O ) ) )
   return datas
   if 4 - 4: I1IiiI % oO0ooO
   if 10 - 10: oO0o0ooO0 . OoooooooOO - OoO0O00 + oO0o0ooO0 - O0
   if 82 - 82: o00ooo0 + II111iiii
  II1i1i1iII1 = values . get ( "report_define" )
  iI1I11iiI1i = I11iii . get_machine_code ( ) or ''
  if 68 - 68: Oo0Ooo + i11iIiiIii
  Oo0oOooo000OO = {
 "template" : "" ,
 "ver" : 4 ,
 "Copies" : values . get ( "print_copies" , 1 ) ,
  "Duplex" : 0 ,
 "mcode" : iI1I11iiI1i ,
 "Tables" : [ ]
 }
  if 98 - 98: o0oOOo0O0Ooo + O0 % i1IIi - ii11ii1ii + Oo0Ooo
  if II1i1i1iII1 . printer_id and II1i1i1iII1 . printer_id != '' :
   Oo0oOooo000OO [ "printer" ] = II1i1i1iII1 . printer_id . name
   if 84 - 84: O0 * OoooooooOO - oO0o0ooO0 * oO0o0ooO0
  i1ii = self . _context . get ( "is_design" , False )
  if i1ii :
   Oo0oOooo000OO [ "design" ] = True
   oO0O = O00o0OO0000oo % ( _ ( """请在康虎云报表设计器设计报表。<br/>
            如果报表设计器未打开，请检查康虎云报表是否已启动！<br/><br/><br/>
            模板设计完成后，请在odoo菜单“康虎云报表”--&gt;“模板”菜单中，打开模板记录上传或更新模板！<br/><br/>
            <a href=\"cfprint://open\">启动康虎云报表</a>
            """ ) )
   values . update ( show_message = oO0O )
   if 86 - 86: OoOoOO00 . iIii1I11I1II1 - OoO0O00
  if II1i1i1iII1 . use_client_templ and II1i1i1iII1 . client_templ_name :
   Oo0oOooo000OO [ "template" ] = II1i1i1iII1 . client_templ_name
  else :
   if not II1i1i1iII1 . template_id or not II1i1i1iII1 . template_id . templ_id :
    values . update ( show_message = O00o0OO0000oo % ( _ ( "未指定要打印的报表模板，请先指定报表模板。" ) ) )
   oOO = self . env [ 'cf.template' ] . search ( [ ( 'templ_id' , '=' , II1i1i1iII1 . template_id . templ_id ) ] , limit = 1 ) . template
   if not oOO or oOO == "" :
    if not i1ii :
     values . update ( show_message = O00o0OO0000oo % ( _ ( "指定的报表模板未定义或模板无内容，请先设计模板并更新到模板记录表。</h3>" ) ) )
    else :
     Oo0oOooo000OO [ "template" ] = "cf_templ_%s" % ( II1i1i1iII1 . name . replace ( '.' , '_' ) )
   else :
    Oo0oOooo000OO [ "template" ] = "base64:" + oOO . strip ( ) . decode ( "UTF-8" ) . replace ( "\n" , "" )
    if 31 - 31: ii11ii1ii / Oo0Ooo * i1IIi . OoOoOO00
  O0O0Oo00 = values . get ( "docs" )
  if not O0O0Oo00 or len ( O0O0Oo00 ) < 1 :
   OO0o0oO = self . _context . get ( "active_ids" , [ ] )
   O0O0Oo00 = self . env [ II1i1i1iII1 . model_id . model ] . browse ( OO0o0oO )
   if 83 - 83: o0oOOo0O0Ooo / i11iIiiIii % iIii1I11I1II1 . oO0ooO % OOooOOo . OoooooooOO
  OooOOOO = { }
  ooo0O = time . clock ( )
  iii11 ( II1i1i1iII1 , II1i1i1iII1 . model_id , II1i1i1iII1 . field_ids , O0O0Oo00 , OooOOOO )
  II1i = time . clock ( )
  print ( "_make_data_obj consume:  %f" % ( II1i - ooo0O ) )
  if 94 - 94: iI1Ii11111iIi + iIii1I11I1II1 % OoO0O00
  if 93 - 93: iI1Ii11111iIi - ii11ii1ii + iIii1I11I1II1 * o0oOOo0O0Ooo + iiIIIII1i1iI . ii1II11I1ii1I
  for IiI1iII1II111 , ( IIiI11i1111Ii , o00O0O ) in enumerate ( OooOOOO . items ( ) ) :
   if 70 - 70: Oo0Ooo . OoOoOO00
   O00o00O = IIiI11i1111Ii . replace ( "." , "_" )
   oO0o00oOOooO0 = o00O0O [ "cols" ]
   ii1iii11i1 = o00O0O [ "rows" ]
   Oo0oOooo000OO [ "Tables" ] . append ( {
 "Name" : O00o00O ,
 "Cols" : oO0o00oOOooO0 ,
 "Data" : ii1iii11i1 ,
 } )
   if 4 - 4: oO0o0ooO0 . oO0o0ooO0 % I1ii11iIi11i % iI1Ii11111iIi / iI1Ii11111iIi
  return Oo0oOooo000OO
  if 29 - 29: Oo0Ooo * o00ooo0 * I1ii11iIi11i / i11iIiiIii
 def _set_report_data ( self , values , report_data ) :
  if 26 - 26: oO0o0ooO0 % iiIIIII1i1iI % OOooOOo % iI1Ii11111iIi
  if 55 - 55: o00ooo0 % OoooooooOO / OoooooooOO % OoooooooOO
  II1i1i1iII1 = values . get ( "report_define" )
  if 52 - 52: I1ii11iIi11i + I1ii11iIi11i . II111iiii
  Iii = "127.0.0.1"
  IIIII1iii = 54321
  IIiiii = self . env [ "cf.print.server.user.mapping" ] . search ( [ ( 'user_id' , '=' , self . env . user . id ) ] , limit = 1 )
  if IIiiii and IIiiii . prn_server_ip :
   Iii = IIiiii . prn_server_ip
   if IIiiii . prn_server_port and IIiiii . prn_server_port > 0 and IIiiii . prn_server_port < 65535 : IIIII1iii = IIiiii . prn_server_port
  else :
   Iii = II1i1i1iII1 . prn_server_address or "127.0.0.1"
   IIIII1iii = II1i1i1iII1 . prn_server_port if II1i1i1iII1 . prn_server_port and II1i1i1iII1 . prn_server_port > 0 and II1i1i1iII1 . prn_server_port < 65535 else 54321
   if 37 - 37: o0oOOo0O0Ooo % o00ooo0
   if 83 - 83: ii11ii1ii . iiIIIII1i1iI + OOooOOo - ii11ii1ii * iiIIIII1i1iI / iiIIIII1i1iI
  I11I1 = [
 'var cfprint_addr = \"%s\"' % ( Iii ) ,
 'var cfprint_port = %d' % ( IIIII1iii ) ,
 "var _delay_close = -1"
 ]
  O00ooOO . debug ( 'Dump report data to json...' )
  iiI1i1Iii111 = json . dumps ( report_data , ensure_ascii = False )
  if 43 - 43: o0oOOo0O0Ooo
  if 71 - 71: OOooOOo % oO0ooO * OoOoOO00 . O0 / iI1Ii11111iIi . I1ii11iIi11i
  O00ooOO . debug ( 'Encrypt report data...' )
  ooOOoooooo = I11iii . rand_aes_key ( 16 , False )
  O00ooOO . debug ( "AES Key: %s" % ( ooOOoooooo ) )
  oOOOo = I11iii ( ooOOoooooo , AES . MODE_CBC )
  ooo0O = time . clock ( )
  OO0O0o0o0 = oOOOo . encrypt ( iiI1i1Iii111 )
  II1i = time . clock ( )
  print ( "Encrypt consume: %f" % ( II1i - ooo0O ) )
  if 31 - 31: iI1Ii11111iIi
  if 44 - 44: OoOoOO00 - iIii1I11I1II1 - Oo0Ooo
  O00ooOO . debug ( 'Encrypt key...' )
  if 80 - 80: iIii1I11I1II1 * iiIIIII1i1iI % oO0ooO % Oo0Ooo
  if 95 - 95: iIii1I11I1II1 - I1ii11iIi11i . iiIIIII1i1iI - I1IiiI
  if 75 - 75: OoO0O00 + o0oOOo0O0Ooo - i1IIi . OoooooooOO * iI1Ii11111iIi / oO0o0ooO0
  if 86 - 86: OoOoOO00 * II111iiii - O0 . OoOoOO00 % iIii1I11I1II1 / ii11ii1ii
  oOOOo = I11iii ( oo0Ooo0 ( ) , AES . MODE_CBC )
  IiIIiIIIiIii = oOOOo . encrypt ( ooOOoooooo )
  if 23 - 23: ii1II11I1ii1I + oO0ooO . OoOoOO00 * I1IiiI + I1ii11iIi11i
  I1iIi1iiiIiI = {
 "token" : IiIIiIIIiIii . decode ( "utf-8" ) ,
 "dea" : "aes" ,
  "tea" : "aes" ,
  "data" : OO0O0o0o0 . decode ( "utf-8" )
 }
  if 41 - 41: I1ii11iIi11i * o00ooo0 - iI1Ii11111iIi + Oo0Ooo
  O00ooOO . debug ( 'Dump final_data...' )
  if 23 - 23: II111iiii % o0oOOo0O0Ooo + o0oOOo0O0Ooo + ii1II11I1ii1I - ii1II11I1ii1I
  I11I1 . append ( "var _data = %s" % ( json . dumps ( I1iIi1iiiIiI , ensure_ascii = False ) ) )
  if 62 - 62: o0oOOo0O0Ooo
  I11I1 . append ( """_reportData = JSON.stringify(_data);\nconsole.log(_reportData);""" )
  if 45 - 45: ii11ii1ii * o00ooo0
  if 74 - 74: i1IIi + O0 + Oo0Ooo
  if II1i1i1iII1 . back_after_print :
   I11I1 . append ( """
            function _delay(ms) { return new Promise(resolve => setTimeout(resolve, ms)); } \n 
            _delay(1000).then(() => window.history.go(-1));  /*延迟一秒后返回到上一页*/""" )
  iIIIi1i1I11i = ";\n" . join ( I11I1 )
  O00ooOO . debug ( 'json_data: %s ...' % ( iIIIi1i1I11i [ 0 : 300 ] ) )
  if 55 - 55: Oo0Ooo - ii11ii1ii
  values . update (
 cfprint_json = iIIIi1i1I11i ,
 )
  if 84 - 84: iiIIIII1i1iI + Oo0Ooo - OoOoOO00 * OoOoOO00
  if 61 - 61: OoooooooOO . OOooOOo . OoooooooOO / Oo0Ooo
 def render ( self , template , values = None ) :
  if values is None :
   if 72 - 72: i1IIi
   if 82 - 82: OoOoOO00 + OoooooooOO / i11iIiiIii * I1ii11iIi11i . OoooooooOO
   if 63 - 63: I1ii11iIi11i
   if 6 - 6: o00ooo0 / I1ii11iIi11i
   if 57 - 57: oO0ooO
   if 67 - 67: OoO0O00 . o00ooo0
   values = { }
   if 87 - 87: OOooOOo % iI1Ii11111iIi
  O00ooOO . debug ( "Render report..." )
  i11i1ii1I = self . _get_report_from_name ( template )
  if not i11i1ii1I :
   raise AccessError ( _ ( "未找到报表（%s）定义，可能是报表未定义或定义未生效，如果使用康虎云报表，请在报表定义中重新生成一下报表定义！" % ( template ) ) )
   if 83 - 83: II111iiii - oO0ooO
  oO0O = O00o0OO0000oo % ( _ ( "正在打印，请稍候...<br/><br/>如果打印机未输出报表，请检查康虎云报表是否已启动！<br/><br/><a href=\"cfprint://open\">启动康虎云报表</a>" ) )
  if 35 - 35: i1IIi - iIii1I11I1II1 + i1IIi
  O00ooOO . debug ( "Prepare docs..." )
  O0O0Oo00 = values . get ( "docs" , False )
  if not O0O0Oo00 or len ( O0O0Oo00 ) < 1 :
   OO0o0oO = self . _context . get ( "active_ids" , [ ] )
   O0O0Oo00 = self . env [ i11i1ii1I . model ] . browse ( OO0o0oO )
   values . update ( docs = O0O0Oo00 )
  if not O0O0Oo00 or len ( O0O0Oo00 ) < 1 :
   oO0O = O00o0OO0000oo % ( _ ( "没有可以打印数据。" ) )
   if 86 - 86: iIii1I11I1II1 + OoOoOO00 . i11iIiiIii - iI1Ii11111iIi
  O00ooOO . debug ( "Retrieve report define..." )
  if 51 - 51: OoOoOO00
  I11IIIiIi11 = i11i1ii1I . xml_id . split ( "." )
  if len ( I11IIIiIi11 ) > 1 :
   I11IIIiIi11 = I11IIIiIi11 [ 1 ] . replace ( iiIi1IIi1I , "" )
  else :
   I11IIIiIi11 = I11IIIiIi11 [ 0 ] . replace ( iiIi1IIi1I , "" )
   if 39 - 39: iI1Ii11111iIi % O0 % OoOoOO00 . i1IIi
  values . update (
 show_message = oO0O
 )
  if 86 - 86: OoO0O00 * OoooooooOO
  if 71 - 71: iIii1I11I1II1 - ii11ii1ii . I1IiiI % OoooooooOO + ii11ii1ii
  IIi11I1 = self . env [ "cf.report.define" ] . search ( [ ( 'name' , '=' , I11IIIiIi11 ) ] , limit = 1 )
  if 49 - 49: II111iiii - I1IiiI / oO0ooO
  O00ooOO . debug ( "Prepare to make json...[%s]" % ( I11IIIiIi11 ) )
  if IIi11I1 :
   O00ooOO . debug ( "Set report_define to values..." )
   values . update ( report_define = IIi11I1 , )
   O00ooOO . debug ( "Begin to make report data ..." )
   O0O0ooOOO = self . _make_cfprint_json ( values )
   O00ooOO . debug ( "Begin to convert report data to json..." )
   self . _set_report_data ( values , O0O0ooOOO )
   O00ooOO . debug ( "Converted!!!" )
   if 70 - 70: o00ooo0 . O0 . iiIIIII1i1iI . O0 + i1IIi
  i1II1I = super ( ii1III11 , self ) . render ( template , values )
  return i1II1I
  if 95 - 95: OoO0O00 - ii11ii1ii / II111iiii % I1ii11iIi11i . o0oOOo0O0Ooo
 def action_upload_templ_win ( self ) :
  ii = self . _context . get ( "templ_id" , False )
  return {
 'name' : _ ( '上传康虎云报表模板' ) ,
 'type' : 'ir.actions.act_window' ,
 'view_type' : 'form' ,
 'res_model' : 'cf.template' ,
 'res_id' : ii ,

  'context' : self . _context ,
 'target' : 'current' ,
 'nodestroy' : True
 }
  if 1 - 1: o00ooo0
 @ api . model
 def render_qweb_html ( self , docids , data = None ) :
  if 78 - 78: I1ii11iIi11i + oO0ooO - O0
  i1I1iIi1IiI = data . get ( "is_design" , False )
  i1111 = _ ( "设计" ) if i1I1iIi1IiI else _ ( "打印" )
  if 82 - 82: o00ooo0 % iI1Ii11111iIi - o00ooo0 % OoOoOO00
  IIi11I1 = self . cf_report_define_id
  if IIi11I1 :
   if not docids :
    docids = data . get ( "docids" , None )
    if 47 - 47: iIii1I11I1II1 . OOooOOo . ii11ii1ii * i1IIi
   oO0O = O00o0OO0000oo % ( _ ( "正在打印，请稍候...<br/><br/>如果打印机未输出报表，请检查康虎云报表是否已启动！<br/><br/><a href=\"cfprint://open\">启动康虎云报表</a>" ) )
   if 32 - 32: i11iIiiIii - i1IIi % ii11ii1ii . O0 % OoOoOO00 * Oo0Ooo
   O0O0Oo00 = data . get ( "docs" , False )
   if 90 - 90: ii11ii1ii * iiIIIII1i1iI
   if ( not O0O0Oo00 or len ( O0O0Oo00 ) < 1 ) and ( not docids or len ( docids ) < 1 ) :
    docids = self . _context . get ( "active_ids" , [ ] )
    if 50 - 50: oO0o0ooO0 % i1IIi
   if ( not O0O0Oo00 or not isinstance ( O0O0Oo00 , list ) or len ( O0O0Oo00 ) < 1 ) and docids and IIi11I1 and IIi11I1 . model_id and IIi11I1 . model_id . model :
    O0O0Oo00 = self . env [ IIi11I1 . model_id . model ] . browse ( docids )
    if 21 - 21: OoooooooOO - iIii1I11I1II1
   if ( not O0O0Oo00 or len ( O0O0Oo00 ) < 1 ) and ( not docids or len ( docids ) < 1 ) :
    oO0O = O00o0OO0000oo % ( _ ( "没有可以%s数据。" ) % ( i1111 ) )
    if 93 - 93: OOooOOo - o0oOOo0O0Ooo % OoOoOO00 . OoOoOO00 - o00ooo0
   data . update ( docs = O0O0Oo00 , show_message = oO0O , )
   if 90 - 90: o00ooo0 + II111iiii * I1ii11iIi11i / iI1Ii11111iIi . o0oOOo0O0Ooo + o0oOOo0O0Ooo
   if IIi11I1 :
    data . update ( report_define = IIi11I1 , )
    ooo0O = time . clock ( )
    O0O0ooOOO = self . with_context ( is_design = i1I1iIi1IiI ) . _make_cfprint_json ( data )
    II1i = time . clock ( )
    print ( "_make_cfprint_json consume:  %f" % ( II1i - ooo0O ) )
    self . _set_report_data ( data , O0O0ooOOO )
    if 40 - 40: o00ooo0 / OoOoOO00 % i11iIiiIii % I1ii11iIi11i / I1IiiI
  return super ( ii1III11 , self ) . render_qweb_html ( docids , data )
  if 62 - 62: i1IIi - OoOoOO00
  if 62 - 62: i1IIi + Oo0Ooo % oO0o0ooO0
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
