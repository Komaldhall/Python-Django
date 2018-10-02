from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker
from django.db.models import Q

def index(request):
	context = {
		"baseball": League.objects.filter(name__icontains="baseball"),
		"women": League.objects.filter(name__icontains="women"),
		"hockey": League.objects.filter(name__icontains="hockey"),
		"not_football": League.objects.exclude(sport__icontains="football"),
		"conferences": League.objects.filter(name__icontains="conference"),
		"atlantic": League.objects.filter(name__icontains="atlantic"),
		"dallas":Team.objects.filter(location__icontains="dallas"),
		"raptors":Team.objects.filter(team_name__icontains="raptors"),
		"city":Team.objects.filter(location__icontains="city"),
		"begin_T":Team.objects.filter(team_name__startswith="T"),
		"alpha":Team.objects.order_by('location'),
		"reverse":Team.objects.order_by('-team_name'),
		"cooper":Player.objects.filter(last_name__icontains='cooper'),
		"joshua":Player.objects.filter(first_name__icontains='joshua'),
		"not_joshua":Player.objects.filter(last_name__icontains='cooper').exclude(first_name__icontains="joshua"),
		"anw":Player.objects.filter(Q(first_name__icontains='alexander')|Q(first_name__icontains='wyatt')),
		
	}
	return render(request, "leagues/index.html", context)


# def index(request):
# 	context = {
# 		"leagues": League.objects.all(),
# 		"teams": Team.objects.all(),
# 		"players": Player.objects.all(),
# 	}
# 	return render(request, "leagues/index.html", context)



def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")