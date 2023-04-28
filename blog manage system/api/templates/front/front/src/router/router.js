import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import luntanfenleiList from '../pages/luntanfenlei/list'
import luntanfenleiDetail from '../pages/luntanfenlei/detail'
import luntanfenleiAdd from '../pages/luntanfenlei/add'
import bokeList from '../pages/boke/list'
import bokeDetail from '../pages/boke/detail'
import bokeAdd from '../pages/boke/add'
import ziyuanfenxiangList from '../pages/ziyuanfenxiang/list'
import ziyuanfenxiangDetail from '../pages/ziyuanfenxiang/detail'
import ziyuanfenxiangAdd from '../pages/ziyuanfenxiang/add'
import ziyuanfenleiList from '../pages/ziyuanfenlei/list'
import ziyuanfenleiDetail from '../pages/ziyuanfenlei/detail'
import ziyuanfenleiAdd from '../pages/ziyuanfenlei/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'luntanfenlei',
					component: luntanfenleiList
				},
				{
					path: 'luntanfenleiDetail',
					component: luntanfenleiDetail
				},
				{
					path: 'luntanfenleiAdd',
					component: luntanfenleiAdd
				},
				{
					path: 'boke',
					component: bokeList
				},
				{
					path: 'bokeDetail',
					component: bokeDetail
				},
				{
					path: 'bokeAdd',
					component: bokeAdd
				},
				{
					path: 'ziyuanfenxiang',
					component: ziyuanfenxiangList
				},
				{
					path: 'ziyuanfenxiangDetail',
					component: ziyuanfenxiangDetail
				},
				{
					path: 'ziyuanfenxiangAdd',
					component: ziyuanfenxiangAdd
				},
				{
					path: 'ziyuanfenlei',
					component: ziyuanfenleiList
				},
				{
					path: 'ziyuanfenleiDetail',
					component: ziyuanfenleiDetail
				},
				{
					path: 'ziyuanfenleiAdd',
					component: ziyuanfenleiAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})
