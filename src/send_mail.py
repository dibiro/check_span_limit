import datetime


general_time_limit = {
    "day": 24*3600,
    "hours": 3600,
    "minute": 60
}

default_limit = [
    {
        "time": "day",
        "limit": 10
    },
    {
        "time": "hours",
        "limit": 3
    },
    {
        "time": "minute",
        "limit": 1
    }
]

general_status = {
    "News": [
        {
            "time": "day",
            "limit": 10
        },
        {
            "time": "hours",
            "limit": 3
        },
        {
            "time": "minute",
            "limit": 1
        }
    ],
    "Status update": [
        {
            "time": "day",
            "limit": 100
        },
        {
            "time": "hours",
            "limit": 20
        },
        {
            "time": "minute",
            "limit": 3
        }
    ],
    "Project invitations": []
}


class SendEmail(object):
    
    def __init__(self):
        self.records = {}
        self.format = '%Y-%m-%d'
        
    def send_email(self):
        return True

    def save_record(self):
        if self.send_email():
            user_records = self.records.get(self.user, {}).get(
                self.date,
                []
            )
            user_records.append(
                {
                    "send_time": self.now,
                    "status": self.status
                }
            )
            self.records[self.user] = {}
            self.records[self.user][self.date] = user_records

    def check_limit(self, status, user, message):
        self.status = status
        self.user = user
        self.message = message
        time_limits = general_status.get(self.status, [])
        if len(time_limits) == 0:
            print('set default time_limits')
            time_limits = default_limit
        self.now = datetime.datetime.now()
        self.date = self.now.strftime(self.format)
        user_records = self.records.get(self.user, {}).get(
            self.date,
            []
        )
        aux_control = False
        for time_limit in time_limits:
            aux_limit = 0
            limit_in_seconds = general_time_limit[time_limit["time"]]
            for user_record in user_records:
                if (
                    user_record["status"] == self.status
                    and (
                        self.now - user_record["send_time"]
                    ).total_seconds() < limit_in_seconds
                ):
                    aux_limit += 1
                if aux_limit >= time_limit['limit']:
                    aux_control = True
                    break
            if aux_control:
                break
        if not aux_control:
            self.save_record()
