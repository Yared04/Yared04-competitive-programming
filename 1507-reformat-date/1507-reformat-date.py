class Solution:
    def reformatDate(self, date: str) -> str:
        months = {'Jan': '01','Feb': '02', 'Mar': '03',
                 'Apr': '04', 'May': '05', 'Jun':'06', 'Jul':'07',
                 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11',
                 'Dec': '12'}
        date = date.split()
        formatted_date = date[-1] + '-'
        formatted_date += months[date[1]] + '-'
        formatted_date += date[0][:2] if len(date[0]) > 3 else '0' + date[0][0:1]
        return formatted_date