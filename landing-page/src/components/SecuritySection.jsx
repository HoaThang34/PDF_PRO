const security = [
  { title: 'Mã hóa 2 đầu', desc: 'File của bạn được mã hóa trong quá trình tải lên và xử lý' },
  { title: 'Tự động xóa file', desc: 'File tự động bị xóa khỏi server sau 24 giờ' },
  { title: 'Đảm bảo riêng tư', desc: 'Chúng tôi không đọc, lưu trữ hoặc chia sẻ file của bạn' },
  { title: 'Kho lưu trữ an toàn', desc: 'Dữ liệu được lưu trữ trên hệ thống đám mây bảo mật' },
]

export default function SecuritySection() {
  return (
    <section className="security-section">
      <div className="container">
        <div className="section-header">
          <h2>Bảo mật và riêng tư</h2>
          <p>Chúng tôi đặt bảo mật lên hàng đầu để bảo vệ file của bạn</p>
        </div>
        <div className="security-grid">
          {security.map((s) => (
            <div key={s.title} className="security-card">
              <div className="security-icon">🛡️</div>
              <h3>{s.title}</h3>
              <p>{s.desc}</p>
            </div>
          ))}
        </div>
        <div className="security-guarantee">
          <div className="guarantee-badge">🔒 256-bit SSL Encryption</div>
          <div className="guarantee-badge">✅ ISO 27001 Certified</div>
          <div className="guarantee-badge">📜 GDPR Compliant</div>
        </div>
      </div>
    </section>
  )
}
