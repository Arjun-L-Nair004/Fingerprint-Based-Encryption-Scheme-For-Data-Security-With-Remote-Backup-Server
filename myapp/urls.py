
from django.urls import path

from myapp import views

urlpatterns = [

    path('admin_home/',views.admin_home),

    path('logout/',views.logout),

    path('login/',views.login),
    path('login_post/',views.login_post),
    path('changepassword/',views.changepassword),
    path('changepswd_post/',views.changepswd_post),
    path('sendreply/<id>',views.sendreply),
    path('sendreply_post/',views.sendreply_post),
    path('viewcomp/',views.viewcomp),
    path('viewcomplaint_post/',views.viewcomplaint_post),
    path('viewfeed/',views.viewfeed),
    path('viewfeed_post/',views.viewfeed_post),
    path('viewrev_rat/',views.viewrev_rat),
    path('viewrev_rat_post/',views.viewrev_rat_post),
    path('viewusers/',views.viewusers),
    path('viewusers_post/',views.viewusers_post),



    path('user_home/',views.user_home),

    path('changepassword_user/',views.changepassword_user),
    path('changepassword_post/',views.changepassword_post),
    path('download/',views.download),
    path('editprofile/',views.editprofile),
    path('editprofile_post/',views.editprofile_post),
    path('sendcomp/',views.sendcomp),
    path('sendcomp_post/',views.sendcomp_post),
    path('sendfeed/',views.sendfeed),
    path('sendfeed_post/',views.sendfeed_post),
    path('sendrev_rat/',views.sendrev_rat),
    path('sendrev_rat_post/',views.sendrev_rat_post),
    path('udetails/',views.udetails),
    path('udetails_post/',views.udetails_post),
    path('upload/',views.upload),
    path('upload_post/',views.upload_post),
    path('viewprof/',views.viewprof),
    path('viewreply/',views.viewreply),
    path('viewreply_post/',views.viewreply_post),
    path('downloadpost/',views.downloadpost),
    path('download_files/<id>',views.download_files),
    path('downloads3/<fid>',views.downloads3),











]
