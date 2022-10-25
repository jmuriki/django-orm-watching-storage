from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from datacenter.models import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
	passcard = get_object_or_404(Passcard, passcode=passcode)
	visits = Visit.objects.filter(passcard=passcard)
	this_passcard_visits = []
	for visit in visits:
		duration = get_duration(visit)
		formatted_duration = format_duration(duration)
		this_passcard_visits.append(
			{
				'entered_at': visit.entered_at,
				'duration': formatted_duration,
				'is_strange': is_visit_long(duration),
			}
		)
	context = {
		'passcard': passcard,
		'this_passcard_visits': this_passcard_visits
	}
	return render(request, 'passcard_info.html', context)
