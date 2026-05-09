from timesheets.backend.storage import Tag, TagSet


last_notification: str = ""


def tags_modified(old: Tag, new: Tag):
    global last_notification

    if not old and new:
        last_notification = "created"

    elif old and not new:
        last_notification = "removed"

    else:
        last_notification = "error"


tag = Tag("TestTag", "A tag to test something")
ts = TagSet()
ts.add_listener(tags_modified)


def test_notify_tag_added():
    ts.add(tag)
    assert last_notification == "created"


def test_nofity_tag_deleted():
    ts.delete(tag)
    assert last_notification == "removed"


def test_listener_removed():
    ts.remove_listener(tags_modified)
    last_notification = "unknown"
    ts.add(tag)
    assert last_notification == "unknown"


def test_tagset_iter():
    ts.clear()

    ts.add(Tag("Tag 1", None))
    ts.add(Tag("Tag 2", None))
    list_tags = [str(tag) for tag in ts]
    assert list_tags == ["Tag 1", "Tag 2"]
