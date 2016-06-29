# QuickJoy

一个非常简单的django+rest_framework+oauth2的小例子

可以通过curl来测试
先通过QuickJoy里的admin登陆上去后.再通过http://localhost:8000/o/applications/ 去新建一个Application

例如:
curl -X POST -d "grant_type=password&client_id=Sp6HFZusPiiXWD6zCE8ZiD908pOssbh154IK1J5M&client_secret=rtaYhKvHyvA8loVb9b6fSjJY5GtdldpmpBgybiJzd6C7tn2GttaSCj6qAb10SRLPNsV8pUofueiyeQk9y6rRKp1MTzdYSAfotDGuGfFudDXgrpXzl8DSP4uLqf2UlgQC&username=sujian&password=1234" http://localhost:8000/o/token/

通过get users拿到所有的user
curl -H "Authorization: Bearer sb2cJ4ezkrrY48bYksVuIX6OwBrRo4" http://localhost:8000/users/
