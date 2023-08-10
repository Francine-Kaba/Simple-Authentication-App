html_body = """
<!doctype html>
<html class="no-js" lang="">
​
<head>
  <meta charset="utf-8">
  <title></title>
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta property="og:title" content="">
  <meta property="og:type" content="">
  <meta property="og:url" content="">
  <meta property="og:image" content="">
  <link rel="manifest" href="site.webmanifest">
  <link rel="apple-touch-icon" href="icon.png">
  <meta name="theme-color" content="#fafafa">
  <style>
    #verifyLink:hover{
        background-color: #344054 !important;
    }
  </style>
</head>
<body style='background-color: white; margin: 0 0 0 0;'>
  <table style="border-width: 0; width:100%; background-color: white" aria-describedby="table1">
    <th>
    <tr>
      <td>
        <table style="background-color: white; max-width:670px; margin:0 auto; width:100%; border:0" aria-describedby="table2">
            <th>
        <tr>
          <td style="padding-top: 4rem; margin-top: 4rem;">
            <table
              style='width: 100%; max-width:670px; background:white; color:#344054; text-align:center; font-weight: 400; font-size: 16px;'
              aria-describedby="table3"
              >
            <th>
              <tr>
                <a href="https://booking-frontend.amalitech-dev.net/">
                  <img src="https://i.ibb.co/WtGV70m/logo.png" alt="logo">
                </a>
              </tr>
              <tr style="display: inline-block">
                <td>
                  <p style='margin-top: 3.5rem; text-align:left;'>Hi {name},</p><br>
                  <p style='line-height:24px; text-align: left'>
                   {body}
                   <br>
                   <b>{extra_detail}</b>
                    <p style="padding-top: 0.5rem; text-align: left;">
                      {instruction}
                    </p>
                    <p style="padding-top: 0.5rem; text-align: left; line-height: 24px">
                      Thanks,<br>Maria team
                    </p>
​                   {% if button%}
                  <a target="_blank" href={{link_url}} id='verifyLink'
                     style='margin-top: 1rem; color: #fff; display:inline-block; text-decoration: none; background: linear-gradient(100.97deg, #6425D3 21.56%, #A259FF 84.43%); padding:15px 120px; border-radius:10px;'>
                    {{button}}
                  </a>
                  {% endif %}
                </td>
              </tr>
            </th>
            </table>
          </td>
        </tr>
        <tr>
          <td style='text-align:left;'>
            <p style='font-size:14px; color:#667085; line-height:18px; margin-top: 3rem;'>
              This email was sent to
              <a style="color: #0408E7">{{email}}</a>
              If you'd rather not receive this kind of email, you can
              <a href="#" style="color: #0408E7">unsubscribe</a> or <a href="#" style="color: #0408E7">manage your email preferences</a>.
              <p style="margin-top: 1rem; font-size:14px; color:#667085; line-height:18px;">&copy;2023 Maria</p>
          </td>
        </tr>
        <tr>
          <td style="display: flex; column-gap: 60%">
            <p>
              <img src="https://i.ibb.co/WtGV70m/logo.png" alt="logo">
            </p>
            <p style="width: max-content;">
              <a href="#"><img alt="twitter" src="https://img.icons8.com/ios-filled/25/98A2B3/twitter.png" style="color: #0408E7"/></a>
              <a href="#"><img alt="facebook" src="https://img.icons8.com/ios-filled/25/98A2B3/facebook-new.png"/></a>
              <a href="#"><img alt="instagram" src="https://img.icons8.com/ios/25/98A2B3/instagram-new--v1.png"/></a>
            </p>
          </td>
        </tr>
    </th>
      </table>
    </td>
  </tr>
</th>
</table>
</body>
</html>

"""
