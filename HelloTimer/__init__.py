import datetime
import logging

import azure.functions as func

from display_time import display_time # 追加した自作ライブラリ

nowtime = display_time.display_time_now()     # 追加
time = nowtime.time_now()                     # 追加
time_str = time.strftime('%Y/%m/%d %H:%M:%S') # 追加

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
    print(f"現在時刻 {time_str}")             # 追加