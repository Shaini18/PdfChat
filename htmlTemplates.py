css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vecteezy.com%2Fpng%2F14456348-cartoon-easter-bunny&psig=AOvVaw3feQ1Es-KuELj1SNylAZON&ust=1694483048846000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCKCVwbW3oYEDFQAAAAAdAAAAABAE" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepnglogos.com%2Fpics%2Fthinking&psig=AOvVaw1Pt2qHQK1hmt_MJ8nzDnLA&ust=1694483182250000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCLCzlPO3oYEDFQAAAAAdAAAAABAE">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
