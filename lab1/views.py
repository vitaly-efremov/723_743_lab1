# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
import random

class IndexView(TemplateView):
	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		stdnts = ['Первый Первый', 'Второй Второй', 'Третий Третий','Четвертый Четвертый', 
                    'Пятый Пятый','Шестой Шестой','Седьмой Седьмой',' Восьмой Восьмой',
                    'Девятый Девятый','Десятый Десятый']
		
		b=len(stdnts)
		bstdnts=[]
		gstdnts=[]
		stts=[]
		
		p_id = student.crt_id(stdnts)
		ss = Score.crt_ss(stdnts)
		
		stts= sort.find(stdnts,ss,gstdnts, bstdnts,stts, p_id) # stdnts, points, P_ids
		
		context.update(
			{
				'students_statistics': stts,
                'excellent_students': gstdnts,
                'bad_students': bstdnts
			}
		)
		return context

class student:
	def crt_id(stdnts):
		p_id=[]
		for i in range(len(stdnts)):
			p_id.append(i)
		return p_id

class sort: # sorting students on bad and good
	def find(stdnts, ss, gstdnts, bstdnts,stts, p_id):
		p=-1
		for i in range(len(stdnts)):
			p=p+1
			if p<=len(stdnts):
				value = Score.crt_value(ss[p])
				if value >=2.7:
					gstdnts.append(stdnts[p])
				
				elif value <=2.7: 
					bstdnts.append(stdnts[p])
				stts.append({ 
				'id': p_id[p]+1,
				'student': stdnts[p],   
				'ТиМП': ss[p]['ТиМП'],
				'ЭиС': ss[p]['ЭиС'],
				'Философия': ss[p]['Философия'], 
				'ИнЯз': ss[p]['ИнЯз'], 
				'Физра': ss[p]['Физ-ра'],   
				'Среднийбал': value}) 	\
		
		return stts
		
   
class Score:
	def crt_ss(stdnts):
		ss=[]
		v=0
		for i in stdnts:
			ss.append({'ТиМП':random.randint(0,5),			'ЭиС':random.randint(0,5), 
						'Философия':random.randint(0,5),	'ИнЯз':random.randint(0,5),
						'Физ-ра':random.randint(0,5)})
			
		return ss

	def crt_value(sss):
		v=0
		for score in sss.values():
			v += score 
		value = v / 5
		return value
    
