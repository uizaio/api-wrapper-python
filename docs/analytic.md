## Analytic

Monitor the four key dimensions of video QoS: playback failures, startup time, rebuffering, and video quality. These 15 metrics help you track playback performance, so your team can know exactly what’s going on.

We can use a `Analytic` to:

- **get_total_line()**
- **get_type()**
- **get_line()**

### Total Line

`get_total_line(start_date, end_date, metric)`

Function to get data grouped by hour (data refresh every 5 minutes). Track video playback on any metric performance, so you can know exactly what’s happening on every user’s device and debug more effectively.

For example:

```python
import uiza

from uiza.api_resources.analytic import Analytic
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Analytic().get_total_line(
        start_date="2018-11-01 20:00",
        end_date="2019-11-02 20:00",
        metric="rebuffer_count"
    )

    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **start_date** (*str*) - Start date (UTC+0) with format: YYYY-MM-DD hh:mm (24-hour clock).
- **end_date** (*str*) - End date (UTC+0) with format: YYYY-MM-DD hh:mm (24-hour clock).
- **metric** (*str*) - You can get data of any metric from [list](https://docs.uiza.io/#analytic-metrics) (use Slug)

#### Return type

- Tuple

#### Return

- Response data and status code

### Type

`get_type(start_date, end_date, type_filter)`

Function to get data base on 4 type of filter: country, device, title, player.

For example:

```python
import uiza

from uiza.api_resources.analytic import Analytic
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Analytic().get_type(
        start_date='2018-11-01 20:00',
        end_date='2019-11-02 20:00',
        type_filter='country'
    )

    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **start_date** (*str*) - Start date (UTC+0) with format: YYYY-MM-DD.
- **end_date** (*str*) - End date (UTC+0) with format: YYYY-MM-DD.
- **type_filter** (*str*) - Value accept: [ country, device, title, player ].

#### Return type

- Tuple

#### Return

- Response data and status code

### Line

`get_line(start_date, end_date)`

Function to get data grouped by hour. Get total view in time range. This help you to draw a line chart to visualize data.

For example:

```python
import uiza

from uiza.api_resources.analytic import Analytic
from uiza.exceptions import ServerException

uiza.workspace_api_domain = "your-workspace-api-domain.uiza.co"
uiza.authorization = "your-authorization"

try:
    res, status_code = Analytic().get_line(
        start_date='2018-11-01 20:00',
        end_date='2019-11-02 20:00',
        type='video_startup_time'
    )

    print("res ", res)
except ServerException as e:
    raise e
except Exception as e:
    raise e
```

#### Parameters

- **start_date** (*str*) - Start date (UTC+0) with format: YYYY-MM-DD.
- **end_date** (*str*) - End date (UTC+0) with format: YYYY-MM-DD.
- **type** (*str*) - Value accept: [ playback_failure_percentage, video_startup_time, aggregate_startup_time, exits_before_video_start, rebuffer_percentage, rebuffer_frequency, playback_failure_score, rebuffer_count, rebuffer_duration, upscale_percentage, downscale_percentage, max_upscale_percentage, max_downscale_percentage ]

#### Return type

- Tuple

#### Return

- Response data and status code
