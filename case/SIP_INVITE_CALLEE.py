com.iad.wait_msg(0,'recv_invite',10)
com.iad.send_msg(0,'send_180')
com.iad.send_msg(0,'send_180_200')
com.iad.wait_msg(0,'recv_ack',5)
com.iad.send_msg(0,'send_bye2')
com.iad.wait_msg(0,'recv_200',5)
