from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .form import *

# flash messages
from django.contrib import messages

# middleware
from unidecode import unidecode
# Create your views here.

# anasayfayı gönder
def index(request):
    context = {}

    posts = Post.objects.all().order_by('-createdAt')

    context['posts'] = posts
    return render(request, 'index.html', context)


# tekil post sayfasını döndür
def post(request, slug):
    context = {}
    form = MakeComment()
    post = Post.objects.get(endPoint=slug)

    if request.method == 'POST':
        form = MakeComment(request.POST)
        if form.is_valid():
            # hata var
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect('singlePost', slug)
    
    else:
        print("yorumlar:", post.yorumlar.all())
        context['post'] = post
        context['form'] = form

    return render(request, 'post-detail.html', context)

# post oluştur
def createPost(request):
    context = {}
    form = MakePost()

    context['blogPost'] = form

    if request.method == 'POST':
        form = MakePost(request.POST)
        if form.is_valid():            
            post = form.save(commit=False)
            # modeli çağır
            content = unidecode(post.title).lower()
            asArray = content.split(' ')
            # post.endPoint = "-".join(asArray)

            duplicatePost = Post.objects.filter(endPoint = "-".join(asArray)).last()
            if duplicatePost:
                # Random sayi verecek algoritma yazilacak.
                id = Post.objects.latest('id')
                print("gelen veri:", id)
                randomId = id.uniqueId()
                randomId += 100
                asArray.append(str(randomId))

            print("GELEN VERİ ARRAY:", asArray)
            post.endPoint = "-".join(asArray)
            post.save()
            
            return redirect('singlePost', post.endPoint)
    else:
        
        return render(request, 'createPost.html', context)


# USER KAYIT OLMAK İSTERSE
def userRegister(request):
 
    if request.method == 'POST':
        
        userName = request.POST.get('u_name')
        userPassword = request.POST.get('u_password')
        userPasswordRepeat = request.POST.get('u_password_repeat')

        if userName and userPassword and userPasswordRepeat:
            isRegistered = User.objects.filter(username=userName, password=userPassword).first()
            if isRegistered: 
                # kullanıcı varsa tekrar kayıt sayfasına yönlendir
                # hata mesajları yapılacak
                return redirect('user-register')
            else:
                # kullanıcıyı oluştur ve login sayfasına yönlendir.
                User.objects.create_user(username=userName, password=userPassword)
                return redirect('user-login')
        else:
            return redirect('user-login')

    else: 
        # bu bir get isteğidir sayfayı yükle
        return render(request, 'register.html')



# Kullanıcı Login Olursa
def userLogin(request):

    if request.method == 'POST':
        uName = request.POST.get('u_name')
        uPassword = request.POST.get('u_password')

        if uName and uPassword:
            user = authenticate(request, username=uName, password=uPassword)

            if user is not None:

               login(request, user)
               return redirect('anasayfa')
            
            else:
                # böyle bir kullanıcı yok
                # hata mesajı ve logine tekrar döndür
                messages.error(request, "Böyle bir kullanıcı bulunamadı.")
                return redirect('user-login')

        else:
            # inputlar doldurulmamışsa
            # kullanıcı adı ve şifre boş bırakılamaz
            messages.error(request, "Kullanıcı adı veya şifre boş bırakılamaz.")
            return redirect('user-login')
    else:
        return render(request, 'login.html')

# kullanıcı logout olursa
def userLogout(request):
    logout(request)
    return redirect('anasayfa')


# yorumları sil
def deleteComment(request, id): 
    endPoint = None
    if request.method == 'POST':
        comment = Comments.objects.get(id=id)
        endPoint = comment.redirectPage

        if comment:
            comment.delete()
            return redirect('/posts/' + endPoint() + "/")
    else:
        return redirect('anasayfa')

# yorumu güncelle
def updateComment(request, id):

     commentObject = Comments.objects.get(id=id)

     if request.method == 'POST':
      
        newMessage = request.POST.get('content')
        commentObject.message = newMessage
        commentObject.save()
            
        return redirect('/posts/' +  commentObject.redirectPage() + "/")

     else:
        # commentForm = UpdateComment()
        return render(request, 'updateComment.html', {'commentObject': commentObject } )