import { IconGithub, IconFacebook, IconMail } from '../icons.jsx'

export default function AuthorSection() {
  return (
    <section className="author-section">
      <div className="container">
        <div className="author-content">
          <div className="author-avatar-wrap">
            <img
              src="/author.png"
              alt="Hoà Quang Thắng"
              className="author-section-avatar"
            />
          </div>
          <h2 className="author-section-name gradient-text">Hoà Quang Thắng</h2>
          <p className="author-section-role">Founder & Developer</p>
          <p className="author-section-bio">
            Tôi tạo ra PDF PRO với sứ mệnh mang đến công cụ xử lý PDF
            chuyên nghiệp, miễn phí và bảo mật cho người Việt.
            Mọi tính năng đều được xây dựng với sự tận tâm và chất lượng cao nhất.
          </p>
          <div className="author-section-links">
            <a href="https://github.com/HoaThang34" target="_blank" rel="noreferrer" className="author-link">
              <IconGithub /> GitHub
            </a>
            <a href="https://www.facebook.com/ThGThanG.734" target="_blank" rel="noreferrer" className="author-link">
              <IconFacebook /> Facebook
            </a>
            <a href="mailto:hoathang34.09@gmail.com" className="author-link">
              <IconMail /> Email
            </a>
          </div>
        </div>
      </div>
    </section>
  )
}
