/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/8.5.66
 * Generated at: 2023-05-07 12:37:46 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp.WEB_002dINF.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class _404_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {

  private static final javax.servlet.jsp.JspFactory _jspxFactory =
          javax.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  private static final java.util.Set<java.lang.String> _jspx_imports_packages;

  private static final java.util.Set<java.lang.String> _jspx_imports_classes;

  static {
    _jspx_imports_packages = new java.util.HashSet<>();
    _jspx_imports_packages.add("javax.servlet");
    _jspx_imports_packages.add("javax.servlet.http");
    _jspx_imports_packages.add("javax.servlet.jsp");
    _jspx_imports_classes = null;
  }

  private volatile javax.el.ExpressionFactory _el_expressionfactory;
  private volatile org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.Map<java.lang.String,java.lang.Long> getDependants() {
    return _jspx_dependants;
  }

  public java.util.Set<java.lang.String> getPackageImports() {
    return _jspx_imports_packages;
  }

  public java.util.Set<java.lang.String> getClassImports() {
    return _jspx_imports_classes;
  }

  public javax.el.ExpressionFactory _jsp_getExpressionFactory() {
    if (_el_expressionfactory == null) {
      synchronized (this) {
        if (_el_expressionfactory == null) {
          _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
        }
      }
    }
    return _el_expressionfactory;
  }

  public org.apache.tomcat.InstanceManager _jsp_getInstanceManager() {
    if (_jsp_instancemanager == null) {
      synchronized (this) {
        if (_jsp_instancemanager == null) {
          _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
        }
      }
    }
    return _jsp_instancemanager;
  }

  public void _jspInit() {
  }

  public void _jspDestroy() {
  }

  public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
      throws java.io.IOException, javax.servlet.ServletException {

    final java.lang.String _jspx_method = request.getMethod();
    if (!"GET".equals(_jspx_method) && !"POST".equals(_jspx_method) && !"HEAD".equals(_jspx_method) && !javax.servlet.DispatcherType.ERROR.equals(request.getDispatcherType())) {
      response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED, "JSP 只允许 GET、POST 或 HEAD。Jasper 还允许 OPTIONS");
      return;
    }

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\r\n");
      out.write("<!DOCTYPE html>\r\n");
      out.write("<html lang=\"en\">\r\n");
      out.write("<head>\r\n");
      out.write("    <meta charset=\"utf-8\">\r\n");
      out.write("    <title>404 Not Find:(</title>\r\n");
      out.write("    <style>\r\n");
      out.write("        ::-moz-selection {\r\n");
      out.write("            background: #b3d4fc;\r\n");
      out.write("            text-shadow: none;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        ::selection {\r\n");
      out.write("            background: #b3d4fc;\r\n");
      out.write("            text-shadow: none;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        html {\r\n");
      out.write("            padding: 30px 10px;\r\n");
      out.write("            font-size: 20px;\r\n");
      out.write("            line-height: 1.4;\r\n");
      out.write("            color: #737373;\r\n");
      out.write("            background: #f0f0f0;\r\n");
      out.write("            -webkit-text-size-adjust: 100%;\r\n");
      out.write("            -ms-text-size-adjust: 100%;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        html,\r\n");
      out.write("        input {\r\n");
      out.write("            font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        body {\r\n");
      out.write("            max-width: 500px;\r\n");
      out.write("            _width: 500px;\r\n");
      out.write("            padding: 30px 20px 50px;\r\n");
      out.write("            border: 1px solid #b3b3b3;\r\n");
      out.write("            border-radius: 4px;\r\n");
      out.write("            margin: 0 auto;\r\n");
      out.write("            box-shadow: 0 1px 10px #a7a7a7, inset 0 1px 0 #fff;\r\n");
      out.write("            background: #fcfcfc;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        h1 {\r\n");
      out.write("            margin: 0 10px;\r\n");
      out.write("            font-size: 50px;\r\n");
      out.write("            text-align: center;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        h1 span {\r\n");
      out.write("            color: #bbb;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        h3 {\r\n");
      out.write("            margin: 1.5em 0 0.5em;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        p {\r\n");
      out.write("            margin: 1em 0;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        ul {\r\n");
      out.write("            padding: 0 0 0 40px;\r\n");
      out.write("            margin: 1em 0;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        .container {\r\n");
      out.write("            max-width: 380px;\r\n");
      out.write("            _width: 380px;\r\n");
      out.write("            margin: 16% auto;\r\n");
      out.write("            text-align: center;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        #goog-fixurl ul {\r\n");
      out.write("            list-style: none;\r\n");
      out.write("            padding: 0;\r\n");
      out.write("            margin: 0;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        #goog-fixurl form {\r\n");
      out.write("            margin: 0;\r\n");
      out.write("        }\r\n");
      out.write("\r\n");
      out.write("        input::-moz-focus-inner {\r\n");
      out.write("            padding: 0;\r\n");
      out.write("            border: 0;\r\n");
      out.write("        }\r\n");
      out.write("    </style>\r\n");
      out.write("</head>\r\n");
      out.write("<body>\r\n");
      out.write("<div class=\"container\">\r\n");
      out.write("    <h1>404 Not Find<span>:(</span></h1>\r\n");
      out.write("    <p>对不起，您访问的页面不存在~</p>\r\n");
      out.write("    <p>请输入正确的地址</p>\r\n");
      out.write("    <p><em id=\"num\">3</em>秒后，自动跳转到上一页</p>\r\n");
      out.write("    <script>\r\n");
      out.write("        var i =3;\r\n");
      out.write("        function djs() {\r\n");
      out.write("            if(i==0){\r\n");
      out.write("                window.history.back();\r\n");
      out.write("            }\r\n");
      out.write("            document.getElementById(\"num\").innerText=i--;\r\n");
      out.write("            setTimeout(\"djs()\",1000);\r\n");
      out.write("        }\r\n");
      out.write("        djs();\r\n");
      out.write("    </script>\r\n");
      out.write("</div>\r\n");
      out.write("</body>\r\n");
      out.write("</html>");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try {
            if (response.isCommitted()) {
              out.flush();
            } else {
              out.clearBuffer();
            }
          } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
