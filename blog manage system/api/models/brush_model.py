# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
# 个人信息
class yonghu(Base_model):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhanghao=db.Column( db.VARCHAR(255), nullable=False,unique=True,comment='账号' )
    mima=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='密码' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    xingbie=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='性别' )
    shouji=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='手机' )
    youxiang=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='邮箱' )
    shenfenzheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='身份证' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )


class luntanfenlei(Base_model):
    __doc__ = u'''luntanfenlei'''
    __tablename__ = 'luntanfenlei'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    luntanfenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='论坛分类' )


class boke(Base_model):
    __doc__ = u'''boke'''
    __tablename__ = 'boke'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    biaoti=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    luntanfenlei=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='论坛分类' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    fabushijian=db.Column( db.Date,  nullable=True, unique=False,comment='发布时间' )
    neirong=db.Column( db.Text,  nullable=True, unique=False,comment='内容' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    sfsh=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )


class ziyuanfenxiang(Base_model):
    __doc__ = u'''ziyuanfenxiang'''
    __tablename__ = 'ziyuanfenxiang'



    __authTables__={'zhanghao':'yonghu',}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='是'
    __intelRecom__='是'
    __browseClick__='是'
    __foreEndListAuth__='否'
    __foreEndList__='是'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    ziyuanmingcheng=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='资源名称' )
    ziyuanfenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='资源分类' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    wenjian=db.Column( db.Text,  nullable=True, unique=False,comment='文件' )
    shangchuanshijian=db.Column( db.Date,  nullable=True, unique=False,comment='上传时间' )
    ziyuanxiangqing=db.Column( db.Text,  nullable=True, unique=False,comment='资源详情' )
    zhanghao=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='账号' )
    xingming=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='姓名' )
    sfsh=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='是否审核' )
    shhf=db.Column( db.Text,  nullable=True, unique=False,comment='审核回复' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )


class ziyuanfenlei(Base_model):
    __doc__ = u'''ziyuanfenlei'''
    __tablename__ = 'ziyuanfenlei'



    __authTables__={}
    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    ziyuanfenlei=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='资源分类' )


class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger,  nullable=True, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='名称' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='类型(1:收藏,21:赞,22:踩,31:竞拍参与,41:关注)' )
    inteltype=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='备注' )


class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    picture=db.Column( db.Text, nullable=False, unique=False,comment='图片' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )


class aboutus(Base_model):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )


class systemintro(Base_model):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False, unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='副标题' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )


class discussboke(Base_model):
    __doc__ = u'''discussboke'''
    __tablename__ = 'discussboke'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )


class discussziyuanfenxiang(Base_model):
    __doc__ = u'''discussziyuanfenxiang'''
    __tablename__ = 'discussziyuanfenxiang'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255),  nullable=True, unique=False,comment='用户名' )
    content=db.Column( db.Text, nullable=False, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )


