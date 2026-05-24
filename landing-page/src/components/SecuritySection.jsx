import { IconShield } from '../icons.jsx'

const security = [
  { title: 'Mã hóa 2 đầu', desc: 'File của bạn được mã hóa trong quá trình tải lên và xử lý bằng giao thức SSL 256-bit' },
  { title: 'Tự động xóa file', desc: 'File tự động bị xóa khỏi server sau 24 giờ, không để lại dấu vết' },
  { title: 'Đảm bảo riêng tư', desc: 'Chúng tôi không đọc, lưu trữ hoặc chia sẻ file của bạn với bất kỳ bên thứ ba nào' },
  { title: 'Kho lưu trữ an toàn', desc: 'Dữ liệu được lưu trữ trên hệ thống đám mây bảo mật đạt chuẩn ISO 27001' },
]

export default function SecuritySection() {
  return (
    <section className="security-section">
      <div className="container">
        <div className="section-header">
          <span className="security-section-icon"><IconShield /></span>
          <h2>Bảo mật và riêng tư</h2>
          <p>Chúng tôi đặt bảo mật lên hàng đầu để bảo vệ file của bạn</p>
        </div>
        <div className="security-grid">
          {security.map((s) => (
            <div key={s.title} className="security-card">
              <div className="security-icon"><IconShield /></div>
              <h3>{s.title}</h3>
              <p>{s.desc}</p>
            </div>
          ))}
        </div>
        <div className="security-guarantee">
          <div className="guarantee-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16"><rect x="3" y="11" width="18" height="11" rx="2" ry="2" /><path d="M7 11V7a5 5 0 0 1 10 0v4" /></svg>
            256-bit SSL Encryption
          </div>
          <div className="guarantee-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16"><polyline points="20 6 9 17 4 12" /></svg>
            ISO 27001 Certified
          </div>
          <div className="guarantee-badge">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16"><circle cx="12" cy="12" r="10" /><path d="M8 12l2 2 4-4" /></svg>
            GDPR Compliant
          </div>
        </div>
      </div>
    </section>
  )
}
