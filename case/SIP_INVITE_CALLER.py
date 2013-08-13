com.iad.send_msg(0,'send_invite')
com.iad.wait_msg(0,'recv_180',5)
com.iad.wait_msg(0,'recv_200',5)
com.iad.send_msg(0,'send_ack')
com.iad.wait_msg(0,'recv_bye',600)
com.iad.send_msg(0,'send_200')
