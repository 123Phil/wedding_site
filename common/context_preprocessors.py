
def is_mobile(request):
	UA_string = str(request.META["HTTP_USER_AGENT"]).lower()
	mobiles = ['mobile', 'iphone', 'android', 'fennec']
	mobile = any(m in UA_string for m in mobiles)
	return {"mobile": mobile}
