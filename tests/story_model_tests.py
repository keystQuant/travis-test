import pytest
from story.models import Story

#### start tests here ####
@pytest.mark.django_db
def test_app_can_create_story_data():
    story_inst = Story(title='test title', story='test story')
    story_inst.save()

    num_of_creates = Story.objects.all().count()
    assert num_of_creates == 1

@pytest.mark.django_db
def test_app_again_can_create_story_data():
    story_inst = Story(title='test title 2', story='test story 2')
    story_inst.save()

    num_of_creates = Story.objects.all().count()
    assert num_of_creates == 1
