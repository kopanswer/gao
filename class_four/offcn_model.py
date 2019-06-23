# --*-- coding:utf8 --*--

from app_data.models.entity import Offcn

class OffcnContent(object):
    def __init__(self):
        """
            record["year"] = year
            record["bureau"] = trs[i].xpath('.//td')[0].xpath('.//a')[0].text
            record["office"] = trs[i].xpath('.//td')[1].text
            record["jobname"] = trs[i].xpath('.//td')[2].xpath('.//a')[0].text
            record["jobcode"] = trs[i].xpath('.//td')[3].text
            record["candidates"] = trs[i].xpath('.//td')[4].text
            record["applicants"] = trs[i].xpath('.//td')[5].text
            record["qualifieds"] = trs[i].xpath('.//td')[6].text
        """
        self.year = ""
        self.bureau = ""
        self.office = ""
        self.jobname = ""
        self.jobcode = ""
        self.candidates = ""
        self.applicants = ""
        self.qualifieds = ""

    def save(self):
        Offcn.objects.update_or_create(
            #   过滤条件，是否等于
            year = self.year,
            bureau = self.bureau,
            office = self.office,
            jobname = self.jobname,
            jobcode = self.jobcode,
            defaults=dict(
                candidates=self.candidates,
                applicants=self.applicants,
                qualifieds=self.qualifieds,
            )
        )

