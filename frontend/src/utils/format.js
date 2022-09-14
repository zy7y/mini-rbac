import moment from 'moment'

export const formatTime = (value) => {
  return moment(value).format('YYYY-MM-DD HH:mm:ss')
}
