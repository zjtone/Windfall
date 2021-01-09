
def get_by_id(model, _id):
    return model.objects.filter(id=_id).get()
