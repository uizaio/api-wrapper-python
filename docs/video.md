## Entity

This is client for calling to API take action with your media files (we called Entity) See details [here](https://docs.uiza.io/#video).

We can use a `Entity` to:
- **create()**
- **retrieve()**
- **list()**
- **update()**
- **delete()**
- **search()**
- **publish()**
- **get_status_publish_entity()**
- **get_aws_upload_key()**


### Create entity

`create(**kwang)` [[source]]()

Function to create entity using full URL. Direct HTTP, FTP or AWS S3 link are acceptable.

For example:
```python
from uiza import Connection
from uiza.api_resources.entity import Entity

connection = Connection(workspace_api_domain=<your-workspace-api-domain.uiza.co>, api_key=<your-api-key>)
entity = Entity(connection)

entity_data = {
        "name": "Sample Video Python1",
        "url": "https://example.com/video.mp4",
        "inputType": "http",
        "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'\''s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    }

res, status_code = entity.create(**entity_data)

# or 
# res, status_code = entity.create(
#   name="Sample Video Python1",
#   url="https://example.com/video.mp4",
#   inputType="http",
#   "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry'\''s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# )

print("id: ", res.id)
print("status_code", status_code)
```

### Parameters
- **name** (*str*) - Name of entity.
- **url** (*str*) - Full URL of media file (direct public HTTP/HTTPS, FTP, AWS S3 acceptable). Send empty string in case of integration using SDK upload to AWS.
- **inputType** (*str*) - Type of URL (Allowed value: [ http, s3, ftp, s3-uiza ] ). In case url is empty string, this must be s3-uiza.
- **description** (*str*) - Full description for entity (without max-length).
- **metadataId** (*list*) - Add relation between entity and folder/playlist.
- **shortDescription** (*str*) - Short description of entity (250 characters).
- **poster** (*str*) - Poster of entity.
- **thumbnail** (*str*) - Thumbnail of entity.
- **metadataIds** (*list*) - List of category will be attached with entity.
- **extendMetadata** (*dict*) - Additional information of entity.
- **embedMetadata** (*dict*) - See [Embed Metadata](https://docs.uiza.io/#embed-metadata) for more information.

### Return type
- Tuple

### Return
- Response data and status code


