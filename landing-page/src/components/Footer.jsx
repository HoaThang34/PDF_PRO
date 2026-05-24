const footerLinks = {
  'Sản phẩm': ['Tính năng', 'Bảng giá', 'Tải app', 'API Docs', 'Trình duyệt'],
  'Công cụ': ['Merge PDF', 'Split PDF', 'Compress PDF', 'OCR PDF', 'Edit PDF'],
  'Hỗ trợ': ['Trợ giúp', 'Liên hệ', 'Báo cáo lỗi', 'Yêu cầu tính năng'],
  'Pháp lý': ['Chính sách bảo mật', 'Điều khoản sử dụng', 'Cookie Policy'],
}

export default function Footer() {
  return (
    <footer className="footer" id="footer">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-brand">
            <div className="logo">
              <div className="logo-icon">P</div>
              <span className="logo-text">PDF PRO</span>
            </div>
            <p className="footer-desc">
              Công cụ xử lý PDF chuyên nghiệp, miễn phí và bảo mật.
              Được phát triển bởi đội ngũ kỹ sư tâm huyết.
            </p>
            <div className="footer-social">
              <a href="#!" className="social-link" aria-label="Facebook">f</a>
              <a href="#!" className="social-link" aria-label="GitHub">G</a>
              <a href="#!" className="social-link" aria-label="YouTube">▶</a>
              <a href="#!" className="social-link" aria-label="Twitter">𝕏</a>
            </div>
          </div>

          {Object.entries(footerLinks).map(([title, links]) => (
            <div key={title} className="footer-col">
              <h4>{title}</h4>
              <ul>
                {links.map((l) => (
                  <li key={l}><a href="#!">{l}</a></li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="footer-bottom">
          <p>© 2024 PDF PRO. Tất cả quyền được bảo lưu.</p>
          <p>
            Liên hệ: <a href="mailto:hello@pdfpro.com">hello@pdfpro.com</a> |
            <a href="https://github.com/HoaThang34/PDF_PRO" target="_blank" rel="noreferrer"> GitHub</a>
          </p>
        </div>
      </div>
    </footer>
  )
}
