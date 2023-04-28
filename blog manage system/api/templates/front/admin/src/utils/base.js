const base = {
    get() {
        return {
            url : "http://localhost:8080/python0ebx7/",
            name: "python0ebx7",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "博客管理系统"
        } 
    }
}
export default base
