import { IconFacebook, IconGithub, IconMail, IconPhone } from '../icons.jsx'

export default function Footer() {
  return (
    <footer className="footer" id="footer">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-brand">
            <div className="logo">
              <img src="/logo.png" alt="PDF PRO" className="logo-img" />
              <span className="logo-text">PDF PRO</span>
            </div>
            <p className="footer-desc">
              Công cụ xử lý PDF chuyên nghiệp, miễn phí và bảo mật.
              Được phát triển bởi đội ngũ kỹ sư tâm huyết với sứ mệnh mang đến
              giải pháp xử lý PDF tốt nhất cho người Việt.
            </p>

            <div className="footer-author">
              <div className="author-card">
                <img
                  src="/hoaquangthang.png"
                  alt="Hoà Quang Thắng"
                  className="author-avatar"
                />
                <div>
                  <div className="author-name">Hoà Quang Thắng</div>
                  <div className="author-role">Founder & Developer</div>
                </div>
              </div>
            </div>
          </div>

          <div className="footer-col">
            <h4>Công cụ</h4>
            <ul>
              <li><a href="#tools">Ghép file PDF</a></li>
              <li><a href="#tools">Tách trang PDF</a></li>
              <li><a href="#tools">Nén file PDF</a></li>
              <li><a href="#tools">Chuyển đổi PDF</a></li>
              <li><a href="#tools">Chỉnh sửa PDF</a></li>
              <li><a href="#tools">OCR PDF</a></li>
            </ul>
          </div>

          <div className="footer-col">
            <h4>Liên hệ</h4>
            <ul className="footer-contact">
              <li>
                <a href="https://www.facebook.com/ThGThanG.734" target="_blank" rel="noreferrer">
                  <span className="contact-icon"><IconFacebook /></span>
                  Facebook
                </a>
              </li>
              <li>
                <a href="https://github.com/HoaThang34" target="_blank" rel="noreferrer">
                  <span className="contact-icon"><IconGithub /></span>
                  GitHub
                </a>
              </li>
              <li>
                <a href="mailto:hoathang34.09@gmail.com">
                  <span className="contact-icon"><IconMail /></span>
                  hoathang34.09@gmail.com
                </a>
              </li>
              <li>
                <a href="tel:0389823083">
                  <span className="contact-icon"><IconPhone /></span>
                  0389 823 083
                </a>
              </li>
            </ul>
          </div>

          <div className="footer-col">
            <h4>Pháp lý</h4>
            <ul>
              <li><a href="#!">Chính sách bảo mật</a></li>
              <li><a href="#!">Điều khoản sử dụng</a></li>
              <li><a href="#!">Cookie Policy</a></li>
            </ul>
          </div>
        </div>

        <div className="footer-bottom">
          <p>© 2026 PDF PRO. Tất cả quyền được bảo lưu.</p>
          <p>
            <a href="https://github.com/HoaThang34/PDF_PRO" target="_blank" rel="noreferrer">
              <IconGithub /> GitHub
            </a>
          </p>
        </div>
      </div>
    </footer>
  )
}
