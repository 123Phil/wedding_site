
def is_mobile(request):
	UA_string = str(request.META["HTTP_USER_AGENT"]).lower()
	mobile = any(m in UA_string for m in ['mobile', 'iphone', 'android', 'fennec'])
	return {"is_mobile": mobile}
