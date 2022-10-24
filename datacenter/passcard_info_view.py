from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django.shortcuts import get_object_or_404

from datacenter.models import get_duration
from datacenter.models import format_duration
from datacenter.models import is_visit_long


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
				'duration': str(duration).split(".")[0],
				'is_strange': is_visit_long(formatted_duration),
			}
		)
	context = {
		'passcard': passcard,
		'this_passcard_visits': this_passcard_visits
	}
	return render(request, 'passcard_info.html', context)
