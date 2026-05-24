import { IconPDF, IconImage, IconText, IconExcel, IconRotate, IconShield, IconArrowRight, IconCheck } from '../icons.jsx'

const steps = [
  {
    icon: IconUploadAnimated,
    title: 'Tải file PDF lên',
    desc: 'Chọn file từ máy tính hoặc kéo thả trực tiếp vào ứng dụng.',
    detail: 'Hỗ trợ tất cả phiên bản PDF, dung lượng lên đến 2GB.',
  },
  {
    icon: IconWandAnimated,
    title: 'Xử lý tự động',
    desc: 'AI phân tích và áp dụng các tác vụ bạn chọn một cách thông minh.',
    detail: 'Nhận dạng cấu trúc, tối ưu hình ảnh, giữ nguyên định dạng.',
  },
  {
    icon: IconDownloadAnimated,
    title: 'Tải xuống kết quả',
    desc: 'File PDF hoàn chỉnh được xuất ra với chất lượng tốt nhất.',
    detail: 'Không mất dữ liệu, không watermark, bảo mật tuyệt đối.',
  },
]

function IconUploadAnimated() {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="animated-icon" width="32" height="32">
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
      <polyline points="17 8 12 3 7 8" />
      <line x1="12" y1="3" x2="12" y2="15" />
      <circle cx="12" cy="16" r="1" fill="currentColor" opacity="0.3">
        <animate attributeName="opacity" values="0.3;0.8;0.3" dur="2s" repeatCount="indefinite" />
      </circle>
    </svg>
  )
}

function IconWandAnimated() {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="animated-icon" width="32" height="32">
      <path d="M15 4V2" />
      <path d="M15 16v-2" />
      <path d="M8 9h2" />
      <path d="M20 9h2" />
      <path d="M17.8 11.8L19 13" />
      <path d="M15 9a.5.5 0 0 0-1 0v4a.5.5 0 0 0 1 0V9z" />
      <circle cx="15" cy="9" r="5" />
      <path d="M4 20l7-7" />
      <line x1="3" y1="21" x2="4" y2="20" />
      <line x1="10" y1="14" x2="11" y2="13" />
      <animateTransform attributeName="transform" type="rotate" values="0 15 9;5 15 9;0 15 9" dur="3s" repeatCount="indefinite" />
    </svg>
  )
}

function IconDownloadAnimated() {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="animated-icon" width="32" height="32">
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
      <polyline points="7 10 12 15 17 10">
        <animate attributeName="opacity" values="1;0.5;1" dur="2.5s" repeatCount="indefinite" />
      </polyline>
      <line x1="12" y1="15" x2="12" y2="3" />
    </svg>
  )
}

function BeforeAfterIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="20" height="20">
      <circle cx="7" cy="12" r="4" stroke="#ef4444" />
      <circle cx="17" cy="12" r="4" stroke="#22c55e" />
      <line x1="11" y1="12" x2="13" y2="12" stroke="#666" />
    </svg>
  )
}

export default function DemoSection() {
  return (
    <section className="demo-section" id="demo">
      <div className="container">
        <div className="section-header">
          <h2>Quy trình xử lý PDF chuyên nghiệp</h2>
          <p>Trải nghiệm quy trình xử lý PDF mượt mà với 3 bước đơn giản</p>
        </div>

        <div className="demo-flow">
          {steps.map((s, i) => (
            <div key={i} className="demo-flow-step">
              <div className="demo-flow-icon"><s.icon /></div>
              <div className="demo-flow-content">
                <h3>{s.title}</h3>
                <p>{s.desc}</p>
                <span className="demo-flow-detail">{s.detail}</span>
              </div>
              {i < steps.length - 1 && (
                <div className="demo-flow-arrow"><IconArrowRight /></div>
              )}
            </div>
          ))}
        </div>

        <div className="demo-before-after">
          <div className="section-header" style={{ marginBottom: 32 }}>
            <h3 style={{ fontSize: '1.5rem', color: '#fff', fontWeight: 700 }}>
              <BeforeAfterIcon /> Chất lượng trước và sau khi xử lý
            </h3>
            <p>Công nghệ AI tự động tối ưu và nâng cao chất lượng file PDF của bạn</p>
          </div>

          <div className="ba-comparison">
            <div className="ba-card ba-before">
              <div className="ba-label">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16"><circle cx="12" cy="12" r="10" /><line x1="12" y1="8" x2="12" y2="12" /><line x1="12" y1="16" x2="12.01" y2="16" /></svg>
                Trước khi xử lý
              </div>
              <div className="ba-preview ba-preview--bad">
                <div className="ba-file-info">
                  <IconPDF /> <span>Tài liệu_quét.pdf</span>
                </div>
                <div className="ba-stats">
                  <div className="ba-stat"><span className="ba-stat-label">Kích thước</span><span className="ba-stat-value">24.6 MB</span></div>
                  <div className="ba-stat"><span className="ba-stat-label">Số trang</span><span className="ba-stat-value">12</span></div>
                  <div className="ba-stat"><span className="ba-stat-label">Chất lượng</span><span className="ba-stat-warn">Kém</span></div>
                </div>
                <div className="ba-issues">
                  <div className="ba-issue">Hình ảnh mờ, nhiễu scan</div>
                  <div className="ba-issue">Văn bản không thể chọn/chỉnh sửa</div>
                  <div className="ba-issue">File quá nặng, khó gửi qua email</div>
                  <div className="ba-issue">Thiếu OCR, không search được nội dung</div>
                </div>
                <div className="ba-quality-bar">
                  <div className="ba-quality-fill ba-quality-fill--low" style={{ width: '25%' }} />
                </div>
              </div>
            </div>

            <div className="ba-arrow-column">
              <div className="ba-arrow-circle">
                <IconArrowRight />
              </div>
              <div className="ba-arrow-text">Xử lý AI</div>
            </div>

            <div className="ba-card ba-after">
              <div className="ba-label">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" width="16" height="16"><polyline points="20 6 9 17 4 12" /></svg>
                Sau khi xử lý
              </div>
              <div className="ba-preview ba-preview--good">
                <div className="ba-file-info">
                  <IconPDF /> <span>Tài_liệu_đã_xử_lý.pdf</span>
                </div>
                <div className="ba-stats">
                  <div className="ba-stat"><span className="ba-stat-label">Kích thước</span><span className="ba-stat-value">3.2 MB</span></div>
                  <div className="ba-stat"><span className="ba-stat-label">Số trang</span><span className="ba-stat-value">12</span></div>
                  <div className="ba-stat"><span className="ba-stat-label">Chất lượng</span><span className="ba-stat-good">Tuyệt vời</span></div>
                </div>
                <div className="ba-issues ba-issues--good">
                  <div className="ba-issue ba-issue--fixed">Hình ảnh sắc nét, đã khử nhiễu</div>
                  <div className="ba-issue ba-issue--fixed">Văn bản đã OCR, có thể chỉnh sửa</div>
                  <div className="ba-issue ba-issue--fixed">Nén thông minh, giảm 87% dung lượng</div>
                  <div className="ba-issue ba-issue--fixed">Có thể tìm kiếm nội dung bằng từ khóa</div>
                </div>
                <div className="ba-quality-bar">
                  <div className="ba-quality-fill ba-quality-fill--high" style={{ width: '95%' }} />
                </div>
              </div>
            </div>
          </div>

          <div className="demo-stats-row">
            <div className="demo-stat-mini">
              <span className="demo-stat-mini-value">87%</span>
              <span className="demo-stat-mini-label">Giảm dung lượng</span>
            </div>
            <div className="demo-stat-mini">
              <span className="demo-stat-mini-value">12x</span>
              <span className="demo-stat-mini-label">Tăng tốc độ xử lý</span>
            </div>
            <div className="demo-stat-mini">
              <span className="demo-stat-mini-value">99%</span>
              <span className="demo-stat-mini-label">Độ chính xác OCR</span>
            </div>
          </div>
        </div>

        <div className="demo-features-showcase">
          <div className="showcase-grid">
            <div className="showcase-item">
              <span className="showcase-icon"><IconImage /></span>
              <div>
                <h4>Trích xuất hình ảnh</h4>
                <p>Xuất tất cả hình ảnh từ PDF sang PNG/JPEG với độ phân giải gốc</p>
              </div>
            </div>
            <div className="showcase-item">
              <span className="showcase-icon"><IconText /></span>
              <div>
                <h4>Trích xuất văn bản</h4>
                <p>Trích xuất toàn bộ nội dung văn bản từ PDF một cách chính xác</p>
              </div>
            </div>
            <div className="showcase-item">
              <span className="showcase-icon"><IconExcel /></span>
              <div>
                <h4>Xuất sang Excel</h4>
                <p>Chuyển đổi bảng biểu trong PDF sang file Excel có định dạng</p>
              </div>
            </div>
            <div className="showcase-item">
              <span className="showcase-icon"><IconRotate /></span>
              <div>
                <h4>Sắp xếp trang</h4>
                <p>Xoay, sắp xếp lại thứ tự trang PDF theo ý muốn một cách trực quan</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}
