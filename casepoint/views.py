from django.shortcuts import render, HttpResponse,redirect
from django.views.generic import View
from .forms import CaseTitleForm, CaseContentForm
from .models import CaseType, CaseTitle, CaseContent, CaseIdeaTitle, CaseIdeaContent

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
#新增case
class CaseAdd(View):

    def get(self, request):
        forms = CaseTitleForm()
        return render(request, 'casepoint/caseadd.html', locals())

    def post(self, request):
        caseContentNum = request.POST.get("caseContentNum") #问题个数
        casetitle=request.POST.get("title")
        casetypeid = request.POST.get("caseType")
        CaseTitleInstance = CaseTitle()
        CaseTitleInstance.title=casetitle
        CaseTitleInstance.caseType_id = casetypeid
        # CaseTitleInstance.user=request.user
        CaseTitleInstance.save()
        for i in range(int(caseContentNum)):
            ccInstance=CaseContent()
            # ccInstance.CaseTitleid = CaseTitle.objects.get(title=casetitle)
            ccInstance.title_id = CaseTitleInstance.id
            ccInstance.Contents=request.POST.get("casecontent"+str(i+1))
            ccInstance.save()
        return  redirect(to='caselist')


#查看所有case
def caseList(request):
    allCaseTitle=CaseTitle.objects.all()
    context ={}
    context['allCaseTitle'] = allCaseTitle
    return render(request,'casepoint/index.html',context)

#分类下case信息
#查看case详情
def caseDiscrib(request,id):
    v_ct = CaseTitle.objects.get(pk=id)
    # case内容
    v_cc = CaseContent.objects.values("Contents").filter(title_id=id)
    # casidea主题 ，方案主题名称
    v_cit = CaseIdeaTitle.objects.values("title", "user","id").distinct().filter(caseTitle_id=id)
    context ={}
    context['ct'] = v_ct
    context['cc'] = v_cc
    context['cit'] = v_cit
    return render(request,'casepoint/casediscrib.html',context)


# 新建方案
class IdeaAdd(View):
    def get(self, request, id):
        casetitle = CaseTitle.objects.get(pk=id)
        ccSet = CaseContent.objects.filter(title_id=id)
        context = {}
        context['casetitle'] = casetitle
        context['ccSet'] = ccSet
        return render(request, 'casepoint/IdeaAdd.html', context)

    def post(self,request,id):
        Num = request.POST.get("Num")  # CASE 步骤数
        CTid = request.POST.get("CT_id")
        citInstance = CaseIdeaTitle()
        citInstance.title = request.POST.get("IdeaTitle")
        citInstance.caseTitle_id = CTid
        # CaseTitleInstance.user=request.user
        citInstance.save()
        citInstance_id = citInstance.id
        for i in range(int(Num)):
            # ccId=request.POST.get("cc_content"+str(i+1))
            # cicContent = request.POST.get("cc_text" + str(i + 1))
            cicInstance = CaseIdeaContent()
            cicInstance.title_id = citInstance_id
            cicInstance.caseContent_id = request.POST.get("cc_content"+str(i+1))
            cicInstance.contents = request.POST.get("cc_text" + str(i + 1))
            cicInstance.parentI_id = 0
            cicInstance.createTime = '2019-01-01 10:10:10'
            cicInstance.updateTime = '2019-01-01 10:10:10'
            # cicInstance.user = request.user
            cicInstance.save()
        return redirect(to='caselist')


#查看方案内容： 获取 CaseIdeaTitle 表id
def ideaDetil(request,ctid,itid):
    casetitle = CaseTitle.objects.get(pk=ctid)
    casecontents = CaseContent.objects.filter(title_id=ctid)
    caseideatitle = CaseIdeaTitle.objects.get(caseTitle_id=ctid)
    caseideacontents = CaseIdeaContent.objects.filter(title_id=caseideatitle.id)
    context ={}
    context['casetitle'] = casetitle
    context['casecontents'] = casecontents
    context['caseideatitle'] = caseideatitle
    context['caseideacontents'] = caseideacontents
    return render(request,'casepoint/ideaDetil.html',context)
