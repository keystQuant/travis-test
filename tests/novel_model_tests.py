import pytest
from novel.models import Novel

#### start tests here ####
@pytest.mark.django_db
def test_app_can_create_novel_data():
    novel_inst = Novel(title='test title', novel='test novel')
    novel_inst.save()

    num_of_creates = Novel.objects.all().count()
    assert num_of_creates == 1
